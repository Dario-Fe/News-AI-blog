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

def fetch_markdown_files():
    """
    Recursively fetches all markdown file details from the GitHub repository.
    """
    print("Fetching all markdown files...")
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    response = requests.get(GITHUB_API_URL, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching root articles list: {response.status_code}")
        return []

    all_md_files = []
    # Process top-level directories (each representing an article container)
    for item in response.json():
        if item['type'] == 'dir':
            dir_url = item['url']
            dir_contents_response = requests.get(dir_url, headers=headers)
            if dir_contents_response.status_code == 200:
                dir_contents = dir_contents_response.json()
                for file_item in dir_contents:
                    name = file_item['name']
                    # We only care about Italian .md files for the main build
                    if name.endswith('.md') and not name.endswith(('_en.md', '_es.md', '_fr.md', '_de.md')):
                        # Add parent directory info to the file object for later use
                        file_item['parent_dir'] = item['name']
                        all_md_files.append(file_item)
            else:
                print(f"Warning: Could not fetch contents of {item['name']}")

    print(f"Found {len(all_md_files)} markdown files to process.")
    return all_md_files

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

    # 2. Fetch all markdown files from GitHub API
    md_files = fetch_markdown_files()
    if not md_files:
        print("No markdown files found. Exiting.")
        return

    # 3. Process all articles from the markdown files
    processed_articles = []
    # Sort files by name case-insensitively ascending to get parts in order
    s1 = sorted(md_files, key=lambda x: x['name'].lower())
    # Then sort by parent directory descending to get newest article groups first
    sorted_md_files = sorted(s1, key=lambda x: x['parent_dir'], reverse=True)

    for md_file in sorted_md_files:
        article_data = process_article(md_file)
        if article_data:
            processed_articles.append(article_data)

    # 4. Generate individual article pages
    generate_article_pages(processed_articles)

    # 4. Generate index page
    generate_index_page(processed_articles)

    # 5. Generate RSS feed
    generate_rss_feed(processed_articles)


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
