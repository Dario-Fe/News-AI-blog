import re
import os

with open('build.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add translations
search_trans = """    "search": {
        "placeholder": {
            "it": "Cerca articoli...",
            "en": "Search articles...",
            "es": "Buscar artículos...",
            "fr": "Rechercher des articles...",
            "de": "Artikel suchen..."
        },
        "label": {
            "it": "Cerca",
            "en": "Search",
            "es": "Buscar",
            "fr": "Rechercher",
            "de": "Suchen"
        },
        "no_results": {
            "it": "Nessun risultato trovato",
            "en": "No results found",
            "es": "No se han trovato risultati",
            "fr": "Aucun résultat trovato",
            "de": "Keine Ergebnisse gefunden"
        }
    },"""
content = re.sub(r'("subscribe": \{.*?\n\s+\},)', r'\1\n' + search_trans, content, flags=re.DOTALL)

# 2. Add lang to articles.json
content = content.replace("article_copy = {k: v for k, v in article.items() if k != 'html_content'}",
                        "article_copy = {k: v for k, v in article.items() if k != 'html_content'}\n        article_copy['lang'] = lang")

# 3. Add data-is-home to articles grid
content = content.replace('grid_html = \'<div id="articles-grid">\\n\'', 'grid_html = \'<div id="articles-grid" data-is-home="true">\\n\'')

# 4. Define unified replacement logic in all functions
funcs = [
    ('generate_article_pages', 1),
    ('generate_author_pages', 2),
    ('generate_index_page', 1),
    ('generate_local_pages', 1),
    ('generate_404_page', 1)
]

for func, depth in funcs:
    replaces = f"""        temp_html = temp_html.replace("{{{{lang}}}}", lang)
        temp_html = temp_html.replace("{{{{depth}}}}", "{depth}")
        temp_html = temp_html.replace("{{{{search_placeholder}}}}", TRANSLATIONS["search"]["placeholder"].get(lang, TRANSLATIONS["search"]["placeholder"]["it"]))
        temp_html = temp_html.replace("{{{{search_label}}}}", TRANSLATIONS["search"]["label"].get(lang, TRANSLATIONS["search"]["label"]["it"]))
        temp_html = temp_html.replace("{{{{search_no_results}}}}", TRANSLATIONS["search"]["no_results"].get(lang, TRANSLATIONS["search"]["no_results"]["it"]))"""

    if func == 'generate_index_page':
        replaces = replaces.replace('        ', '    ')

    target = 'temp_html = temp_html.replace("{{subscribe_link_text}}", TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"]))'
    if target in content:
        # Avoid double replacement if script is re-run
        if f'temp_html.replace("{{{{depth}}}}", "{depth}")' not in content:
             content = content.replace(target, target + '\n' + replaces)

with open('build.py', 'w', encoding='utf-8') as f:
    f.write(content)

# 5. Fix templates/base.html
with open('templates/base.html', 'r', encoding='utf-8') as f:
    base = f.read()

search_ui = """                <div id="search-container">
                    <button id="search-toggle" class="search-toggle" title="{{search_label}}"></button>
                    <div id="search-input-wrapper" class="search-input-wrapper">
                        <input type="text" id="search-input" placeholder="{{search_placeholder}}" aria-label="{{search_label}}">
                        <div id="search-results" class="search-results"></div>
                    </div>
                </div>"""
if '<div id="search-container">' not in base:
    base = base.replace('<div id="language-selector-container">', '<div id="language-selector-container">\n' + search_ui)

if 'searchNoResultsText' not in base:
    base = base.replace("placeholderImage: '{{placeholder_image_path}}'",
                       "placeholderImage: '{{placeholder_image_path}}',\n        searchNoResultsText: '{{search_no_results}}'")

search_js = r"""
            /**
             * Loads the articles JSON index for search if not already loaded.
             */
            const ensureSearchIndexLoaded = async () => {
                if (searchIndexLoaded) return;
                try {
                    const depth = parseInt('{{depth}}' || '1');
                    const prefix = "../".repeat(depth - 1);
                    const response = await fetch(`${prefix}articles.json`);
                    if (!response.ok) throw new Error('Network response was not ok');
                    allArticles = await response.json();
                    searchIndexLoaded = true;
                } catch (error) {
                    console.error('Failed to load search index:', error);
                }
            };

            /**
             * Performs search and updates results dropdown.
             */
            const performSearch = (query) => {
                if (!query || query.length < 2) {
                    searchResults.style.display = 'none';
                    searchResults.innerHTML = '';
                    return;
                }

                const normalizedQuery = query.toLowerCase().trim();
                const currentLang = window.APP_CONFIG.lang;
                const filteredResults = allArticles.filter(article => {
                    if (article.lang && article.lang !== currentLang) return false;
                    return (article.title && article.title.toLowerCase().includes(normalizedQuery)) ||
                           (article.summary && article.summary.toLowerCase().includes(normalizedQuery)) ||
                           (article.tags && article.tags.some(tag => tag.toLowerCase().includes(normalizedQuery)));
                }).slice(0, 8);

                renderSearchResults(filteredResults);
            };

            /**
             * Renders results into the dropdown.
             */
            const renderSearchResults = (results) => {
                searchResults.innerHTML = '';
                if (results.length === 0) {
                    searchResults.innerHTML = `<div class="search-no-results">${window.APP_CONFIG.searchNoResultsText}</div>`;
                } else {
                    const depth = parseInt('{{depth}}' || '1');
                    const prefix = "../".repeat(depth - 1);
                    const assetPrefix = "../".repeat(depth);
                    results.forEach(article => {
                        const item = document.createElement('a');
                        item.href = prefix + article.path;
                        item.className = 'search-result-item';

                        let imageHtml = '';
                        if (article.image_paths) {
                            imageHtml = `<img src="${assetPrefix}${article.image_paths.thumb_jpeg}" alt="">`;
                        }

                        item.innerHTML = `
                            ${imageHtml}
                            <div class="search-result-info">
                                <div class="search-result-title">${article.title}</div>
                                <div class="search-result-summary">${article.summary}</div>
                            </div>
                        `;
                        searchResults.appendChild(item);
                    });
                }
                searchResults.style.display = 'block';
            };
"""

if 'ensureSearchIndexLoaded' not in base:
    base = base.replace('// --- DOM Elements ---', 'let searchIndexLoaded = false;\n            // --- DOM Elements ---')
    base = base.replace('const filterButtons = document.querySelectorAll(\'.tag-filter-button\');',
                       "const filterButtons = document.querySelectorAll('.tag-filter-button');\n            const searchToggle = document.getElementById('search-toggle');\n            const searchInputWrapper = document.getElementById('search-input-wrapper');\n            const searchInput = document.getElementById('search-input');\n            const searchResults = document.getElementById('search-results');")
    base = base.replace('// --- Core Functions ---', '// --- Core Functions ---' + search_js)

search_listeners = """
                // Search UI Handlers
                if (searchToggle) {
                    searchToggle.addEventListener('click', async () => {
                        const isOpen = searchInputWrapper.classList.contains('open');
                        if (!isOpen) {
                            await ensureSearchIndexLoaded();
                            searchInputWrapper.classList.add('open');
                            searchInput.focus();
                        } else {
                            searchInputWrapper.classList.remove('open');
                            searchResults.style.display = 'none';
                        }
                    });
                }

                if (searchInput) {
                    searchInput.addEventListener('input', (e) => {
                        performSearch(e.target.value);
                    });

                    searchInput.addEventListener('keydown', (e) => {
                        if (e.key === 'Escape') {
                            searchInputWrapper.classList.remove('open');
                            searchResults.style.display = 'none';
                        }
                    });
                }

                document.addEventListener('click', (e) => {
                    const container = document.getElementById('search-container');
                    if (container && !container.contains(e.target)) {
                        if (searchInputWrapper) searchInputWrapper.classList.remove('open');
                        if (searchResults) searchResults.style.display = 'none';
                    }
                });
"""
if 'Search UI Handlers' not in base:
    base = base.replace('const initialize = async () => {', 'const initialize = async () => {\n' + search_listeners)

base = base.replace('if (grid) {', 'if (grid && grid.hasAttribute(\'data-is-home\')) {')
if 'searchIndexLoaded = true;' not in base:
    base = base.replace('allArticles = await response.json();', 'allArticles = await response.json();\n                        searchIndexLoaded = true;')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base)

# 6. Add style.css
styles = """
        /* Search Bar Styles */
        #search-container {
            display: flex;
            align-items: center;
            position: relative;
        }
        .search-toggle {
            background: none;
            border: none;
            cursor: pointer;
            width: 32px;
            height: 32px;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.7;
            transition: opacity 0.2s;
        }
        .search-toggle:hover {
            opacity: 1;
        }
        .search-toggle::before {
            content: '';
            display: block;
            width: 20px;
            height: 20px;
            background-color: #2c3e50;
            -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E");
            mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E");
            -webkit-mask-size: contain;
            mask-size: contain;
        }
        .search-input-wrapper {
            position: absolute;
            right: 100%;
            top: 50%;
            transform: translateY(-50%);
            width: 0;
            overflow: hidden;
            transition: width 0.3s ease, padding 0.3s ease;
            display: flex;
            align-items: center;
            background: white;
            z-index: 1001;
        }
        .search-input-wrapper.open {
            width: 250px;
            padding: 0 10px;
            overflow: visible;
        }
        #search-input {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #dddfe2;
            border-radius: 20px;
            font-size: 0.8em;
            outline: none;
        }
        .search-results {
            position: absolute;
            top: 100%;
            right: 0;
            width: 300px;
            background: white;
            border: 1px solid #dddfe2;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            margin-top: 10px;
            display: none;
            max-height: 400px;
            overflow-y: auto;
            z-index: 1002;
        }
        .search-result-item {
            display: flex;
            padding: 10px;
            gap: 10px;
            text-decoration: none;
            color: inherit;
            border-bottom: 1px solid #f0f2f5;
            transition: background 0.2s;
        }
        .search-result-item:hover {
            background-color: #f0f2f5;
        }
        .search-result-item img {
            width: 50px;
            height: 50px;
            object-fit: cover;
            border-radius: 4px;
            flex-shrink: 0;
        }
        .search-result-info {
            display: flex;
            flex-direction: column;
            justify-content: center;
            overflow: hidden;
        }
        .search-result-title {
            font-weight: bold;
            font-size: 0.9em;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .search-result-summary {
            font-size: 0.75em;
            color: #606770;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        .search-no-results {
            padding: 20px;
            text-align: center;
            color: #606770;
            font-size: 0.9em;
        }
        @media (max-width: 768px) {
            .search-input-wrapper.open {
                position: fixed;
                top: 60px;
                left: 10px;
                right: 10px;
                width: auto;
                transform: none;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                border-radius: 8px;
                padding: 10px;
            }
            .search-results {
                width: 100%;
                position: fixed;
                top: 110px;
                left: 10px;
                right: 10px;
                width: calc(100% - 20px);
            }
        }
"""
with open('style.css', 'r', encoding='utf-8') as f:
    style_content = f.read()
if 'Search Bar Styles' not in style_content:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(styles)
