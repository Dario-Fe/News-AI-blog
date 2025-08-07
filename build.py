import os
import requests
import frontmatter
import shutil
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
import markdown2

# Constants
GITHUB_API_URL = "https://api.github.com/repos/matteobaccan/CorsoAIBook/contents/articoli"
SITE_URL = "https://<YOUR_USERNAME>.github.io/<YOUR_REPO>/" # We will replace this later
OUTPUT_DIR = "dist"

# It's recommended to use a GitHub token to avoid rate limiting.
# Create a Personal Access Token (PAT) with 'repo' scope and set it as an environment variable.
# For local development: export GITHUB_TOKEN='your_token_here'
# In GitHub Actions, this can be set as a secret.
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

def fetch_articles_list():
    """
    Fetches the list of articles (directories) from the GitHub repository.
    """
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.get(GITHUB_API_URL, headers=headers)

    if response.status_code == 403:
        print("GitHub API rate limit exceeded. Please use a GITHUB_TOKEN.")
        # Fallback to unauthenticated request, which might also be rate limited
        response = requests.get(GITHUB_API_URL)

    if response.status_code != 200:
        print(f"Error fetching articles list: {response.status_code}")
        print(f"Response: {response.text}")
        return []

    articles = [item for item in response.json() if item['type'] == 'dir']
    print(f"Found {len(articles)} articles.")
    return articles

def main():
    """
    Main function to build the static site and RSS feed.
    """
    print("Starting build process...")

    # Create/clean output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # 1. Copy static assets
    copy_static_assets()

    # 2. Fetch articles from GitHub API
    articles = fetch_articles_list()
    if not articles:
        print("No articles found. Exiting.")
        return

    # 2. Process all articles
    processed_articles = []
    # Sort articles by name descending to get newest first
    sorted_articles = sorted(articles, key=lambda x: x['name'], reverse=True)

    for article_dir in sorted_articles:
        article_data = process_article(article_dir)
        if article_data:
            processed_articles.append(article_data)

    # 3. Generate individual article pages
    generate_article_pages(processed_articles)

    # 4. Generate index page
    generate_index_page(processed_articles)

    # 5. Generate RSS feed
    generate_rss_feed(processed_articles)


def process_article(article_dir):
    """
    Fetches the content of a single article, parses it, and returns a dict.
    """
    print(f"Processing article: {article_dir['name']}...")

    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    dir_contents_response = requests.get(article_dir["url"], headers=headers)
    if dir_contents_response.status_code != 200:
        print(f"  Error fetching content for {article_dir['name']}")
        return None

    dir_contents = dir_contents_response.json()

    md_file = next((f for f in dir_contents if f['name'].endswith('.md') and '_en' not in f['name'] and '_es' not in f['name']), None)

    if not md_file:
        print(f"  Markdown file not found in {article_dir['name']}")
        return None

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
                img['src'] = f"https://raw.githubusercontent.com/matteobaccan/CorsoAIBook/main/articoli/{article_dir['name']}/{img['src']}"

        # Get the first image for the summary card
        main_image_url = soup.find('img')['src'] if soup.find('img') else None

        # Get the final HTML content after modifications
        final_html_content = str(soup)

        slug = article_dir['name']

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

def generate_article_pages(articles):
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

        with open(os.path.join(OUTPUT_DIR, article['path']), "w") as f:
            f.write(final_page_html)

def generate_index_page(articles):
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

    with open(os.path.join(OUTPUT_DIR, "index.html"), "w") as f:
        f.write(final_page_html)

def copy_static_assets():
    """
    Copies static assets from the root to the output directory.
    """
    print("\nCopying static assets...")
    static_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js']
    for item in os.listdir('.'):
        if os.path.isfile(item) and any(item.endswith(ext) for ext in static_extensions):
            print(f"  - {item}")
            shutil.copy(item, os.path.join(OUTPUT_DIR, item))

def generate_rss_feed(articles):
    """
    Generates an RSS feed from the list of articles.
    """
    print("\nGenerating RSS feed...")
    fg = FeedGenerator()
    fg.title('Notizie IA - Aggiornamenti e Analisi')
    fg.link(href=SITE_URL, rel='alternate')
    fg.description('Le ultime notizie e approfondimenti sull\'intelligenza artificiale, a cura di Verbania Notizie.')
    fg.language('it')

    for article in articles:
        fe = fg.add_entry()
        fe.title(article['title'])
        fe.link(href=f"{SITE_URL}{article['path']}")
        fe.description(article['summary'])
        # fe.pubDate() # We could add pubDate if we can parse it from the article name or metadata

    fg.rss_file(os.path.join(OUTPUT_DIR, 'rss.xml'), pretty=True)
    print("  - rss.xml")

    print("Build process finished successfully!")

if __name__ == "__main__":
    main()
