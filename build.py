import os
import requests
import frontmatter
import shutil
import argparse
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
import markdown2

# Constants
GITHUB_API_URL = "https://api.github.com/repos/matteobaccan/CorsoAIBook/contents/articoli"
SITE_URL = "https://<YOUR_USERNAME>.github.io/<YOUR_REPO>/" # We will replace this later
BASE_OUTPUT_DIR = "dist"

# It's recommended to use a GitHub token to avoid rate limiting.
# Create a Personal Access Token (PAT) with 'repo' scope and set it as an environment variable.
# For local development: export GITHUB_TOKEN='your_token_here'
# In GitHub Actions, this can be set as a secret.
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

def get_all_repo_files():
    """
    Gets a flat list of all files in the repo using the recursive tree API.
    This is much more efficient than making multiple API calls.
    """
    print("Fetching file tree from GitHub...")
    # Get the main branch name
    repo_info_url = "https://api.github.com/repos/matteobaccan/CorsoAIBook"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    repo_info = requests.get(repo_info_url, headers=headers).json()
    main_branch = repo_info.get('default_branch', 'main')

    # Get the tree recursively
    tree_url = f"https://api.github.com/repos/matteobaccan/CorsoAIBook/git/trees/{main_branch}?recursive=1"
    tree_response = requests.get(tree_url, headers=headers)
    if tree_response.status_code != 200:
        print("Error fetching repository file tree.")
        return None

    return tree_response.json()['tree']


def structure_articles_by_language(all_files):
    """
    Structures all markdown files by their article group and language.
    """
    articles_db = {}
    for file_info in all_files:
        path = file_info['path']
        if path.startswith('articoli/') and path.endswith('.md'):
            parts = path.split('/')
            if len(parts) == 3: # articoli/DIR/file.md
                article_dir = parts[1]
                filename = parts[2]

                if article_dir not in articles_db:
                    articles_db[article_dir] = {}

                # Determine language
                if filename.endswith('_en.md'):
                    lang = 'en'
                elif filename.endswith('_es.md'):
                    lang = 'es'
                elif filename.endswith('.md'):
                    # This is Italian only if no other lang suffix is present
                    is_base_file = not any(s in filename for s in ['_en.md', '_es.md', '_fr.md', '_de.md'])
                    if is_base_file:
                        lang = 'it'
                    else:
                        continue # Skip other languages like _fr, _de for now
                else:
                    continue

                if lang not in articles_db[article_dir]:
                    articles_db[article_dir][lang] = []

                # Add file info needed for processing
                file_info['name'] = filename
                file_info['parent_dir'] = article_dir
                file_info['download_url'] = f"https://raw.githubusercontent.com/matteobaccan/CorsoAIBook/main/{path}"
                articles_db[article_dir][lang].append(file_info)

    return articles_db

def get_files_for_lang(articles_db, lang='it'):
    """
    Gets all markdown files for a specific language from the structured DB.
    NO FALLBACK. If a translation doesn't exist, it's skipped.
    """
    files_for_lang = []
    for article_dir, languages in articles_db.items():
        if lang in languages:
            for file_info in languages[lang]:
                files_for_lang.append(file_info)

    print(f"Found {len(files_for_lang)} markdown files to process for '{lang}'.")
    return files_for_lang

def main():
    """
    Main function to build the static site and RSS feed.
    """
    parser = argparse.ArgumentParser(description="Build the static site for a specific language.")
    parser.add_argument('--lang', default='it', help='Language to build (e.g., en, es)')
    args = parser.parse_args()

    lang = args.lang
    output_dir = os.path.join(BASE_OUTPUT_DIR, lang)

    print(f"Starting build process for language: '{lang}'...")

    # Create language-specific output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # This is now a global database fetched only once if the script were to run
    # for multiple languages in one go. For now, it's fetched for each run.
    all_files = get_all_repo_files()
    if not all_files:
        return

    articles_db = structure_articles_by_language(all_files)

    md_files = get_files_for_lang(articles_db, lang)

    if not md_files:
        print(f"No markdown files found for language '{lang}'. Exiting.")
        # We still finish successfully, just for an empty site for this lang
        return

    # Process all articles from the markdown files
    processed_articles = []
    # Sort files by name case-insensitively descending to get newest parts first
    s1 = sorted(md_files, key=lambda x: x['name'].lower(), reverse=True)
    # Then sort by parent directory descending to get newest article groups first
    sorted_md_files = sorted(s1, key=lambda x: x['parent_dir'], reverse=True)

    for md_file in sorted_md_files:
        article_data = process_article(md_file)
        if article_data:
            processed_articles.append(article_data)

    # 4. Generate individual article pages
    generate_article_pages(processed_articles, output_dir, lang)

    # 5. Generate index page
    generate_index_page(processed_articles, output_dir, lang)

    # 6. Generate RSS feed
    generate_rss_feed(processed_articles, output_dir, lang)

def create_root_redirect():
    """
    Creates a root index.html to redirect to the default language.
    """
    print("\nCreating root redirect...")
    html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Notizie IA</title>
<meta http-equiv="refresh" content="0; url=it/index.html" />
<script type="text/javascript">
    window.location.href = "it/index.html"
</script>
</head>
<body>
<p>Redirecting to the Italian version of the site... <a href="it/index.html">Click here if you are not redirected.</a></p>
</body>
</html>
"""
    with open(os.path.join(BASE_OUTPUT_DIR, "index.html"), "w") as f:
        f.write(html_content)
    print("  - dist/index.html (redirect)")


def process_article(md_file):
    """
    Fetches the content of a single markdown file, parses it, and returns a dict.
    """
    print(f"Processing file: {md_file['name']} in {md_file['parent_dir']}...")

    md_content_response = requests.get(md_file['download_url'])
    if md_content_response.status_code != 200:
        print(f"  Error downloading markdown for {md_file['name']}")
        return None

    md_content = md_content_response.text

    try:
        post = frontmatter.loads(md_content)
        html_content = markdown2.markdown(post.content, extras=["tables", "fenced-code-blocks", "spoiler"])
        soup = BeautifulSoup(html_content, 'html.parser')

        title = soup.h1.get_text() if soup.h1 else "Titolo non disponibile"

        summary = ""
        first_p = soup.find('p')
        if first_p:
            summary = first_p.get_text()

        # Rewrite image paths to be absolute
        for img in soup.find_all('img'):
            if img['src'] and not img['src'].startswith('http'):
                img['src'] = f"https://raw.githubusercontent.com/matteobaccan/CorsoAIBook/main/articoli/{md_file['parent_dir']}/{img['src']}"

        # Get the first image for the summary card
        main_image_url = soup.find('img')['src'] if soup.find('img') else None

        # Get the final HTML content after modifications
        final_html_content = str(soup)

        # Create a unique slug from the filename
        slug = os.path.splitext(md_file['name'])[0]

        return {
            "title": title,
            "summary": summary,
            "image_url": main_image_url,
            "html_content": final_html_content,
            "slug": slug,
            "path": f"{slug}.html"
        }

    except Exception as e:
        print(f"  Error parsing markdown for {md_file['name']}: {e}")
        return None

def generate_article_pages(articles, output_dir, lang='it'):
    """
    Generates an HTML page for each article.
    """
    print("\nGenerating article pages...")
    with open("templates/base.html", "r") as f:
        base_template = f.read()

    for article in articles:
        print(f"  - {article['path']}")

        # Create a simple view for the article content
        article_view_html = f"""
        <div id="article-view">
            <a href="index.html" class="back-button">Torna indietro</a>
            {article['html_content']}
            <div class="footer-back-button">
                <a href="index.html" class="back-button">Torna indietro</a>
            </div>
        </div>
        """

        final_page_html = base_template.replace("{{content}}", article_view_html)

        with open(os.path.join(output_dir, article['path']), "w") as f:
            f.write(final_page_html)

def generate_index_page(articles, output_dir, lang='it'):
    """
    Generates the main index.html page with a grid of all articles.
    """
    print("\nGenerating index page...")
    with open("templates/base.html", "r") as f:
        base_template = f.read()

    grid_html = '<div id="articles-grid">\n'
    for article in articles:
        card_html = f"""
        <a href="{article['path']}" class="article-card">
            <img src="{article['image_url'] if article['image_url'] else 'logo_vn_ia.png'}" alt="{article['title']}" loading="lazy">
            <div class="article-card-content">
                <h3>{article['title']}</h3>
                <p>{article['summary']}</p>
            </div>
        </a>
        """
        grid_html += card_html
    grid_html += '</div>'

    final_page_html = base_template.replace("{{content}}", grid_html)

    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(final_page_html)

def copy_static_assets(output_dir):
    """
    Copies static assets from the root to the output directory.
    """
    print("\nCopying static assets...")
    static_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js']
    for item in os.listdir('.'):
        if os.path.isfile(item) and any(item.endswith(ext) for ext in static_extensions):
            print(f"  - {item}")
            shutil.copy(item, os.path.join(output_dir, item))

def generate_rss_feed(articles, output_dir, lang='it'):
    """
    Generates an RSS feed from the list of articles.
    """
    print("\nGenerating RSS feed...")
    fg = FeedGenerator()
    fg.title(f'Notizie IA - Aggiornamenti e Analisi ({lang})')
    fg.link(href=f"{SITE_URL}{lang}/", rel='alternate')
    fg.description('Le ultime notizie e approfondimenti sull\'intelligenza artificiale, a cura di Verbania Notizie.')
    fg.language(lang)

    for article in articles:
        fe = fg.add_entry()
        fe.title(article['title'])
        fe.link(href=f"{SITE_URL}{lang}/{article['path']}")
        fe.description(article['summary'])
        # fe.pubDate() # We could add pubDate if we can parse it from the article name or metadata

    fg.rss_file(os.path.join(output_dir, 'rss.xml'), pretty=True)
    print(f"  - rss.xml (for {lang})")

    print("Build process finished successfully!")

if __name__ == "__main__":
    main()
