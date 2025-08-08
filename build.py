import os
import requests
import frontmatter
import shutil
import argparse
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
import markdown2
import math

# Constants
GITHUB_API_URL = "https://api.github.com/repos/matteobaccan/CorsoAIBook/contents/articoli"
SITE_URL = "https://<YOUR_USERNAME>.github.io/<YOUR_REPO>/" # We will replace this later
BASE_OUTPUT_DIR = "dist"

# Translations
TRANSLATIONS = {
    "subtitle": {
        "it": "Notizie ed analisi sull'Intelligenza Artificiale",
        "en": "News and analysis on Artificial Intelligence",
        "es": "Noticias y análisis sobre Inteligencia Artificial"
    },
    "subscribe": {
        "it": "Iscriviti",
        "en": "Subscribe",
        "es": "Suscríbete"
    },
    "newsletter_page": {
        "title": {
            "it": "Iscriviti alla nostra Newsletter",
            "en": "Subscribe to our Newsletter",
            "es": "Suscríbete a nuestro boletín"
        },
        "description": {
            "it": "Rimani aggiornato con le ultime notizie e analisi sull'Intelligenza Artificiale. Inserisci i tuoi dati qui sotto per non perdere neanche un articolo.",
            "en": "Stay updated with the latest news and analysis on Artificial Intelligence. Enter your details below to not miss a single article.",
            "es": "Mantente actualizado con las últimas noticias y análisis sobre Inteligencia Artificial. Ingresa tus datos a continuación para no perderte ni un solo artículo."
        },
        "label_name": {
            "it": "Nome:",
            "en": "Name:",
            "es": "Nombre:"
        },
        "placeholder_name": {
            "it": "Il tuo nome",
            "en": "Your name",
            "es": "Tu nombre"
        },
        "label_email": {
            "it": "Email:",
            "en": "Email:",
            "es": "Correo electrónico:"
        },
        "placeholder_email": {
            "it": "La tua email",
            "en": "Your email",
            "es": "Tu correo electrónico"
        },
        "button_text": {
            "it": "Iscriviti Ora",
            "en": "Subscribe Now",
            "es": "Suscríbete Ahora"
        },
        "privacy_note": {
            "it": "Rispettiamo la tua privacy. I tuoi dati non saranno condivisi con terze parti.",
            "en": "We respect your privacy. Your data will not be shared with third parties.",
            "es": "Respetamos tu privacidad. Tus datos no serán compartidos con terceros."
        }
    },
    "thank_you_page": {
        "title": {
            "it": "Grazie per l'iscrizione!",
            "en": "Thanks for subscribing!",
            "es": "¡Gracias por suscribirte!"
        },
        "heading": {
            "it": "Grazie!",
            "en": "Thank You!",
            "es": "¡Gracias!"
        },
        "paragraph": {
            "it": "La tua iscrizione alla newsletter è stata confermata.",
            "en": "Your subscription to the newsletter has been confirmed.",
            "es": "Tu suscripción al boletín ha sido confirmada."
        },
        "button_text": {
            "it": "Torna alla Home",
            "en": "Back to Home",
            "es": "Volver al Inicio"
        }
    },
    "footer": {
        "curated_by": {
            "it": "A cura di",
            "en": "Curated by",
            "es": "A cargo de"
        },
        "contacts": {
            "it": "Contatti",
            "en": "Contacts",
            "es": "Contacto"
        }
    },
    "pagination": {
        "next": {
            "it": "Articoli Successivi &rarr;",
            "en": "Next Articles &rarr;",
            "es": "Artículos Siguientes &rarr;"
        },
        "prev": {
            "it": "&larr; Articoli Precedenti",
            "en": "&larr; Previous Articles",
            "es": "&larr; Artículos Anteriores"
        }
    }
}

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

    # 7. Generate local pages (like newsletter)
    generate_local_pages(output_dir, lang)

    # 8. Copy static assets
    copy_static_assets(output_dir)

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
        slug = os.path.splitext(md_file['name'])[0].strip()

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

        # Replace placeholders
        subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
        subscribe_text = TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"])
        footer_curated_by = TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"])
        footer_contacts = TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"])

        # Path for pages at root level of language dir
        home_link = "index.html"
        logo_path = "logo_vn_ia.png"

        temp_html = base_template.replace("{{subtitle}}", subtitle)
        temp_html = temp_html.replace("{{subscribe_link_text}}", subscribe_text)
        temp_html = temp_html.replace("{{footer_curated_by}}", footer_curated_by)
        temp_html = temp_html.replace("{{footer_contacts}}", footer_contacts)
        temp_html = temp_html.replace("{{home_link}}", home_link)
        temp_html = temp_html.replace("{{logo_path}}", logo_path)
        temp_html = temp_html.replace("{{pagination_controls}}", "") # No pagination on article pages
        final_page_html = temp_html.replace("{{content}}", article_view_html)

        with open(os.path.join(output_dir, article['path']), "w") as f:
            f.write(final_page_html)

def generate_index_page(articles, output_dir, lang='it'):
    """
    Generates paginated index pages with a grid of articles.
    """
    print("\nGenerating index pages...")
    with open("templates/base.html", "r") as f:
        base_template = f.read()

    ARTICLES_PER_PAGE = 15
    total_pages = math.ceil(len(articles) / ARTICLES_PER_PAGE)

    for page_num in range(1, total_pages + 1):
        start_index = (page_num - 1) * ARTICLES_PER_PAGE
        end_index = start_index + ARTICLES_PER_PAGE
        page_articles = articles[start_index:end_index]

        grid_html = '<div id="articles-grid">\n'
        for article in page_articles:
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

        # Generate pagination controls
        pagination_html = ''
        if page_num > 1:
            prev_path = f"../page/{page_num - 1}/index.html" if page_num > 2 else "../index.html"
            prev_text = TRANSLATIONS["pagination"]["prev"].get(lang, TRANSLATIONS["pagination"]["prev"]["it"])
            pagination_html += f'<a href="{prev_path}" class="prev-button">{prev_text}</a>'

        if page_num < total_pages:
            next_path = f"../page/{page_num + 1}/index.html"
            next_text = TRANSLATIONS["pagination"]["next"].get(lang, TRANSLATIONS["pagination"]["next"]["it"])
            # Add a spacer if there's also a prev button
            spacer = '<div style="flex-grow: 1;"></div>' if page_num > 1 else ''
            pagination_html += f'{spacer}<a href="{next_path}" class="next-button">{next_text}</a>'

        # Replace all placeholders
        subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
        subscribe_text = TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"])
        footer_curated_by = TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"])
        footer_contacts = TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"])

        # Set paths based on page depth
        if page_num == 1:
            home_link = "index.html"
            logo_path = "logo_vn_ia.png"
        else:
            home_link = "../../index.html"
            logo_path = "../../logo_vn_ia.png"

        temp_html = base_template.replace("{{subtitle}}", subtitle)
        temp_html = temp_html.replace("{{subscribe_link_text}}", subscribe_text)
        temp_html = temp_html.replace("{{footer_curated_by}}", footer_curated_by)
        temp_html = temp_html.replace("{{footer_contacts}}", footer_contacts)
        temp_html = temp_html.replace("{{home_link}}", home_link)
        temp_html = temp_html.replace("{{logo_path}}", logo_path)
        temp_html = temp_html.replace("{{content}}", grid_html)
        final_page_html = temp_html.replace("{{pagination_controls}}", pagination_html)

        # Determine output path
        if page_num == 1:
            page_output_dir = output_dir
            output_path = os.path.join(page_output_dir, "index.html")
        else:
            page_output_dir = os.path.join(output_dir, "page", str(page_num))
            output_path = os.path.join(page_output_dir, "index.html")

        if not os.path.exists(page_output_dir):
            os.makedirs(page_output_dir)

        print(f"  - Generating page {page_num} at {output_path}")
        with open(output_path, "w") as f:
            f.write(final_page_html)

def generate_local_pages(output_dir, lang='it'):
    """
    Generates standalone pages from the /pages directory.
    """
    print("\nGenerating local pages...")
    pages_dir = "pages"
    if not os.path.exists(pages_dir):
        return

    with open("templates/base.html", "r") as f:
        base_template = f.read()

    for filename in os.listdir(pages_dir):
        if filename.endswith(".html"):
            print(f"  - {filename}")
            with open(os.path.join(pages_dir, filename), "r") as f:
                page_content = f.read()

            # Replace placeholders in the base template
            subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
            subscribe_text = TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"])
            footer_curated_by = TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"])
            footer_contacts = TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"])

            # Path for pages at root level of language dir
            home_link = "index.html"
            logo_path = "logo_vn_ia.png"

            temp_html = base_template.replace("{{subtitle}}", subtitle)
            temp_html = temp_html.replace("{{subscribe_link_text}}", subscribe_text)
            temp_html = temp_html.replace("{{footer_curated_by}}", footer_curated_by)
            temp_html = temp_html.replace("{{footer_contacts}}", footer_contacts)
            temp_html = temp_html.replace("{{home_link}}", home_link)
            temp_html = temp_html.replace("{{logo_path}}", logo_path)
            temp_html = temp_html.replace("{{pagination_controls}}", "") # No pagination on local pages

            # Replace placeholders in the page content itself
            final_content = page_content
            if filename == "newsletter.html":
                for key, trans_dict in TRANSLATIONS["newsletter_page"].items():
                    placeholder = f"{{{{newsletter_page_{key}}}}}"
                    translation = trans_dict.get(lang, trans_dict["it"])
                    final_content = final_content.replace(placeholder, translation)

                # Inject the hidden language field
                soup = BeautifulSoup(final_content, 'html.parser')
                form = soup.find('form', {'name': 'newsletter'})
                if form:
                    hidden_input = soup.new_tag('input', attrs={'type': 'hidden', 'name': 'language', 'value': lang})
                    form.append(hidden_input)
                    final_content = str(soup)

            if filename == "thank-you.html":
                for key, trans_dict in TRANSLATIONS["thank_you_page"].items():
                    placeholder = f"{{{{thank_you_page_{key}}}}}"
                    translation = trans_dict.get(lang, trans_dict["it"])
                    final_content = final_content.replace(placeholder, translation)

            final_page_html = temp_html.replace("{{content}}", final_content)

            with open(os.path.join(output_dir, filename), "w") as f:
                f.write(final_page_html)

def copy_static_assets(output_dir):
    """
    Copies static assets from the root to the output directory.
    """
    print("\nCopying static assets...")
    static_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js', '.html']
    for item in os.listdir('.'):
        if os.path.isfile(item) and any(item.endswith(ext) for ext in static_extensions):
            # Let's avoid copying the template files themselves if they are in the root
            if item not in ["base.html"]: # Simple exclusion for templates
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
