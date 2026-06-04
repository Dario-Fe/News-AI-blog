import re
import os

with open('build.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Translations
search_trans = """    "search": {
        "placeholder": {
            "it": "Cerca articoli...",
            "en": "Search articles...",
            "es": "Buscar articoli...",
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
            "fr": "Aucun risultato trovato",
            "de": "Keine Ergebnisse gefunden"
        }
    },"""
content = re.sub(r'("subscribe": \{.*?\n\s+\},)', r'\1\n' + search_trans, content, flags=re.DOTALL)

# 2. Dynamic placeholders
# Function to safely insert multiple replacements
def safe_inject(text, func_name, depth):
    # Match the function and the target line
    pattern = f'(def {func_name}.*?temp_html = temp_html\.replace\("{{{{subscribe_link_text}}}}", TRANSLATIONS\["subscribe"\]\.get\(lang, TRANSLATIONS\["subscribe"\]\["it"\]\)\))'

    replaces = f"""
        temp_html = temp_html.replace("{{{{lang}}}}", lang)
        temp_html = temp_html.replace("{{{{depth}}}}", "{depth}")
        temp_html = temp_html.replace("{{{{search_placeholder}}}}", TRANSLATIONS["search"]["placeholder"].get(lang, TRANSLATIONS["search"]["placeholder"]["it"]))
        temp_html = temp_html.replace("{{{{search_label}}}}", TRANSLATIONS["search"]["label"].get(lang, TRANSLATIONS["search"]["label"]["it"]))
        temp_html = temp_html.replace("{{{{search_no_results}}}}", TRANSLATIONS["search"]["no_results"].get(lang, TRANSLATIONS["search"]["no_results"]["it"]))"""

    if func_name == 'generate_index_page':
        replaces = replaces.replace('        ', '    ')

    return re.sub(pattern, r'\1' + replaces, text, flags=re.DOTALL)

for fn, d in [('generate_article_pages', '1'), ('generate_author_pages', '2'), ('generate_index_page', '1'), ('generate_local_pages', '1'), ('generate_404_page', '1')]:
    content = safe_inject(content, fn, d)

# 3. articles.json lang
content = content.replace("article_copy = {k: v for k, v in article.items() if k != 'html_content'}",
                        "article_copy = {k: v for k, v in article.items() if k != 'html_content'}\n        article_copy['lang'] = lang")

# 4. data-is-home
content = content.replace('grid_html = \'<div id="articles-grid">\\n\'', 'grid_html = \'<div id="articles-grid" data-is-home="true">\\n\'')

with open('build.py', 'w', encoding='utf-8') as f:
    f.write(content)

# --- Templates ---
with open('templates/base.html', 'r', encoding='utf-8') as f:
    base = f.read()

ui = """                <div id="search-container">
                    <button id="search-toggle" class="search-toggle" title="{{search_label}}"></button>
                    <div id="search-input-wrapper" class="search-input-wrapper">
                        <input type="text" id="search-input" placeholder="{{search_placeholder}}" aria-label="{{search_label}}">
                        <div id="search-results" class="search-results"></div>
                    </div>
                </div>"""
base = base.replace('<div id="language-selector-container">', '<div id="language-selector-container">\n' + ui)
base = base.replace("placeholderImage: '{{placeholder_image_path}}'", "placeholderImage: '{{placeholder_image_path}}',\n        searchNoResultsText: '{{search_no_results}}'")

js = r"""
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
base = base.replace('// --- State Management ---', 'let searchIndexLoaded = false;\n            // --- State Management ---')
base = base.replace('const filterButtons = document.querySelectorAll(\'.tag-filter-button\');',
                   "const filterButtons = document.querySelectorAll('.tag-filter-button');\n            const searchToggle = document.getElementById('search-toggle');\n            const searchInputWrapper = document.getElementById('search-input-wrapper');\n            const searchInput = document.getElementById('search-input');\n            const searchResults = document.getElementById('search-results');")
base = base.replace('// --- Core Functions ---', '// --- Core Functions ---' + js)

listeners = """
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
base = base.replace('const initialize = async () => {', 'const initialize = async () => {\n' + listeners)
base = base.replace('if (grid) {', 'if (grid && grid.hasAttribute(\'data-is-home\')) {')
base = base.replace('allArticles = await response.json();', 'allArticles = await response.json();\n                        searchIndexLoaded = true;')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base)

# --- CSS ---
css_add = """
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
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_add)

# --- README ---
readme = """# AITalk: Static Site Engine & Content Repository

[![Deployment Status](https://img.shields.io/github/actions/workflow/status/darioferrero/aitalk/deploy.yml?branch=main&label=Deploy)](https://github.com/darioferrero/aitalk/actions)
[![Technology](https://img.shields.io/badge/Engine-Python%20SSG-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Netlify-00ad9f.svg)](https://www.netlify.com/)

AITalk is a professional, high-performance static site generator (SSG) specifically engineered for multi-language news portals focused on Artificial Intelligence. This repository contains the complete source code, automation scripts, and Markdown-based content database.

---

## 🚀 Key Features

### ⚡ Performance & Architecture
- **Pure Python SSG**: Customized build engine (`build.py`) designed for maximum speed and minimal overhead.
- **Atomic Incremental Builds**: Intelligent change detection using SHA-1 hashing ensures only modified content is re-processed.
- **Parallel Processing**: Utilizes `ProcessPoolExecutor` for high-speed HTML generation across multiple CPU cores.

### 🌐 Multilingual Excellence
- **Native Support**: Full localized experiences for **Italian**, **English**, **Spanish**, **French**, and **German**.
- **Live Search**: Integrated high-speed, client-side search engine with language-aware filtering and dynamic path resolution.
- **SEO Optimized**: Language-specific RSS feeds, automated robots.txt generation, and proper OpenGraph/Twitter metadata for every page.

### 🎙️ Multimedia & Engagement
- **Podcast Integration**: Automated detection and integration of language-specific audio (`.mp3`) with a native HTML5 player.
- **YouTube Embedding**: Seamless support for video content within articles.
- **E-Book Engine**: Specialized scripts to compile Markdown articles into professionally formatted PDF/EPUB e-books.
- **Newsletter Automation**: Serverless newsletter subscription system via Netlify Forms.

### 📊 Analytics & Insights
- **Privacy-First Tracking**: Lightweight, cookie-less page view tracking via Netlify Functions and Netlify Blobs.
- **Performance Dashboards**: Real-time statistics monitoring without third-party trackers.

---

## 📂 Project Structure

```text
├── articoli/           # Primary content database (Markdown + Media)
├── content/            # Auxiliary data (Author biographies, profiles)
├── ebook/              # E-book generation suite (Python + CSS)
├── netlify/            # Serverless functions (Stats, Analytics)
├── pages/              # Static informational pages (Legal, Cookies, Method)
├── templates/          # HTML blueprints (Base, Article, Author, 404)
├── public/             # Static assets (Flags, icons, logos)
├── build.py            # Core SSG Engine
├── build.sh            # Global build automation
└── style.css           # Global design system
```

---

## 🛠️ Development Workflow

### Prerequisites
- **Python 3.10+**
- **pip** (Python Package Manager)

### Local Environment Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Build System
- **Full Build (All Languages)**:
  ```bash
  ./build.sh
  ```
- **Targeted Build**:
  ```bash
  python build.py --lang [it|en|es|fr|de]
  ```

### Local Preview
Launch a local development server to inspect the generated site in `dist/`:
```bash
cd dist
python -m http.server 8000
```
Access the portal at: `http://localhost:8000`

---

## 📝 Content Management

### Articles
Every article resides in its own directory within `articoli/`, identified by a numeric prefix for chronological sorting (e.g., `105-slug/`).
- **Translations**: Suffix files with language codes (e.g., `article_en.md`).
- **Media**: Place images and audio files directly in the article folder. The engine handles optimization and format conversion (WebP/JPEG) automatically.

### Authors
Manage author profiles in `content/authors/`. Biographical data supports full Markdown formatting.

---

## ☁️ Deployment & CI/CD
The portal is continuously deployed via **GitHub Actions**. Every push to the main branch triggers an automated build and deployment to **Netlify**. The workflow utilizes advanced caching strategies to ensure rapid deployment times.

---
© 2025 AITalk - Curated by **Dario Ferrero**
"""
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
