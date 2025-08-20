import os
import requests
import frontmatter
import shutil
import argparse
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
import markdown2
import math
from urllib.parse import quote
import locale

# Constants
GITHUB_API_URL = "https://api.github.com/repos/matteobaccan/CorsoAIBook/contents/articoli"
SITE_URL = "https://ianotizie.netlify.app/"
BASE_OUTPUT_DIR = "dist"

# (Keeping the TRANSLATIONS dictionary as is, since it's large and unchanged)
TRANSLATIONS = {
    "subtitle": {
        "it": "Notizie ed analisi sull'Intelligenza Artificiale",
        "en": "News and analysis on Artificial Intelligence",
        "es": "Noticias y análisis sobre Inteligencia Artificial",
        "fr": "Actualités et analyses sur l'intelligence artificielle",
        "de": "Nachrichten und Analysen zur Künstlichen Intelligenz"
    },
    "subscribe": {
        "it": "Iscriviti",
        "en": "Subscribe",
        "es": "Suscríbete",
        "fr": "S'abonner",
        "de": "Abonnieren"
    },
    "newsletter_page": {
        "title": {
            "it": "Iscriviti alla nostra Newsletter",
            "en": "Subscribe to our Newsletter",
            "es": "Suscríbete a nostro boletín",
            "fr": "Abonnez-vous à notre newsletter",
            "de": "Abonnieren Sie unseren Newsletter"
        },
        "description": {
            "it": "Rimani aggiornato con le ultime notizie e analisi sull'Intelligenza Artificiale. Inserisci i tuoi dati qui sotto per non perdere neanche un articolo.",
            "en": "Stay updated with the latest news and analysis on Artificial Intelligence. Enter your details below to not miss a single article.",
            "es": "Mantente actualizado con las últimas noticias y análisis sobre Inteligencia Artificial. Ingresa tus datos a continuación para no perderte ni un solo artículo.",
            "fr": "Restez à jour avec les dernières nouvelles et analyses sur l'Intelligence Artificielle. Entrez vos coordonnées ci-dessous pour ne manquer aucun article.",
            "de": "Bleiben Sie auf dem Laufenden mit den neuesten Nachrichten und Analysen zur Künstlichen Intelligenz. Geben Sie unten Ihre Daten ein, um keinen Artikel zu verpassen."
        },
        "label_name": {
            "it": "Nome:",
            "en": "Name:",
            "es": "Nombre:",
            "fr": "Nom:",
            "de": "Name:"
        },
        "placeholder_name": {
            "it": "Il tuo nome",
            "en": "Your name",
            "es": "Tu nombre",
            "fr": "Votre nom",
            "de": "Ihr Name"
        },
        "label_email": {
            "it": "Email:",
            "en": "Email:",
            "es": "Correo electrónico:",
            "fr": "Email:",
            "de": "E-Mail:"
        },
        "placeholder_email": {
            "it": "La tua email",
            "en": "Your email",
            "es": "Tu correo electrónico",
            "fr": "Votre e-mail",
            "de": "Ihre E-Mail"
        },
        "button_text": {
            "it": "Iscriviti Ora",
            "en": "Subscribe Now",
            "es": "Suscríbete Ahora",
            "fr": "Abonnez-vous maintenant",
            "de": "Jetzt abonnieren"
        },
        "privacy_note": {
            "it": "Rispettiamo la tua privacy. I tuoi dati non saranno condivisi con terze parti.",
            "en": "We respect your privacy. Your data will not be shared with third parties.",
            "es": "Respetamos tu privacidad. Tus datos no serán compartidos con terceros.",
            "fr": "Nous respectons votre vie privée. Vos données ne seront pas partagées avec des tiers.",
            "de": "Wir respektieren Ihre Privatsphäre. Ihre Daten werden nicht an Dritte weitergegeben."
        }
    },
    "thank_you_page": {
        "title": {
            "it": "Grazie per l'iscrizione!",
            "en": "Thanks for subscribing!",
            "es": "¡Gracias por suscribirte!",
            "fr": "Merci de votre inscription!",
            "de": "Vielen Dank für Ihre Anmeldung!"
        },
        "heading": {
            "it": "Grazie!",
            "en": "Thank You!",
            "es": "¡Gracias!",
            "fr": "Merci!",
            "de": "Danke!"
        },
        "paragraph": {
            "it": "La tua iscrizione alla newsletter è stata confermata.",
            "en": "Your subscription to the newsletter has been confirmed.",
            "es": "Tu suscripción al boletín ha sido confirmada.",
            "fr": "Votre inscription à la newsletter a été confirmée.",
            "de": "Ihre Anmeldung für den Newsletter wurde bestätigt."
        },
        "button_text": {
            "it": "Torna alla Home",
            "en": "Back to Home",
            "es": "Volver al Inicio",
            "fr": "Retour à l'accueil",
            "de": "Zurück zur Startseite"
        }
    },
    "footer": {
        "curated_by": {
            "it": "A cura di",
            "en": "Curated by",
            "es": "A cargo de",
            "fr": "Édité par",
            "de": "Kuratiert von"
        },
        "contacts": {
            "it": "Contatti",
            "en": "Contacts",
            "es": "Contacto",
            "fr": "Contacts",
            "de": "Kontakt"
        }
    },
    "pagination": {
        "next": {
            "it": "Articoli Successivi &rarr;",
            "en": "Next Articles &rarr;",
            "es": "Artículos Siguientes &rarr;",
            "fr": "Articles suivants &rarr;",
            "de": "Nächste Artikel &rarr;"
        },
        "prev": {
            "it": "&larr; Articoli Precedenti",
            "en": "&larr; Previous Articles",
            "es": "&larr; Artículos Anteriores",
            "fr": "&larr; Articles précédents",
            "de": "&larr; Vorherige Artikel"
        }
    },
    "article_page": {
        "back_button": {
            "it": "Torna indietro",
            "en": "Go back",
            "es": "Volver",
            "fr": "Retour",
            "de": "Zurück"
        }
    }
}
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
LANGUAGES = ["it", "en", "es", "fr", "de"]

def get_language_links():
    """
    Generates a dictionary of root-relative language links.
    """
    links = {}
    for lang in LANGUAGES:
        links[f"{lang}_link"] = f"/{lang}/"
    return links

def get_all_repo_files():
    print("Fetching file tree from GitHub...")
    repo_info_url = "https://api.github.com/repos/matteobaccan/CorsoAIBook"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    repo_info = requests.get(repo_info_url, headers=headers).json()
    main_branch = repo_info.get('default_branch', 'main')
    tree_url = f"https://api.github.com/repos/matteobaccan/CorsoAIBook/git/trees/{main_branch}?recursive=1"
    tree_response = requests.get(tree_url, headers=headers)
    if tree_response.status_code != 200:
        print("Error fetching repository file tree.")
        return None
    return tree_response.json()['tree']

def structure_articles_by_language(all_files):
    articles_db = {}
    for file_info in all_files:
        path = file_info['path']
        if path.startswith('articoli/') and path.endswith('.md'):
            parts = path.split('/')
            if len(parts) == 3:
                article_dir, filename = parts[1], parts[2]
                if article_dir not in articles_db:
                    articles_db[article_dir] = {}
                lang_map = {'_en.md': 'en', '_es.md': 'es', '_fr.md': 'fr', '_de.md': 'de'}
                lang = next((l for suffix, l in lang_map.items() if filename.endswith(suffix)), None)
                if not lang and filename.endswith('.md') and not any(filename.endswith(s) for s in lang_map.keys()):
                    lang = 'it'
                if lang:
                    if lang not in articles_db[article_dir]:
                        articles_db[article_dir][lang] = []
                    file_info.update({
                        'name': filename,
                        'parent_dir': article_dir,
                        'download_url': f"https://raw.githubusercontent.com/matteobaccan/CorsoAIBook/main/{path}"
                    })
                    articles_db[article_dir][lang].append(file_info)
    return articles_db

def get_files_for_lang(articles_db, lang='it'):
    files_for_lang = [file_info for languages in articles_db.values() if lang in languages for file_info in languages[lang]]
    print(f"Found {len(files_for_lang)} markdown files to process for '{lang}'.")
    return files_for_lang

def process_article(md_file):
    print(f"Processing file: {md_file['name']} in {md_file['parent_dir']}...")
    md_content_response = requests.get(md_file['download_url'])
    if md_content_response.status_code != 200: return None
    md_content = md_content_response.text
    try:
        post = frontmatter.loads(md_content)
        html_content = markdown2.markdown(post.content, extras=["tables", "fenced-code-blocks", "spoiler"])
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.h1.get_text() if soup.h1 else "Titolo non disponibile"
        summary = next((p.get_text() for p in soup.find_all('p') if p.get_text(strip=True) and not p.find('img')), "")
        for img in soup.find_all('img'):
            if img.get('src') and not img['src'].startswith('http'):
                img['src'] = f"https://raw.githubusercontent.com/matteobaccan/CorsoAIBook/main/articoli/{md_file['parent_dir']}/{img['src']}"
        main_image_url = soup.find('img')['src'] if soup.find('img') else None
        slug = os.path.splitext(md_file['name'])[0].strip()
        tags = post.metadata.get('tags', [])
        date_obj = post.metadata.get('date', None)
        return {"title": title, "summary": summary, "image_url": main_image_url, "html_content": str(soup), "slug": slug, "path": f"{slug}.html", "tags": tags, "date": date_obj}
    except Exception as e:
        print(f"  Error parsing markdown for {md_file['name']}: {e}")
        return None

def generate_article_pages(articles, output_dir, lang='it'):
    print("\nGenerating article pages...")
    with open("templates/base.html", "r") as f:
        base_template = f.read()

    for article in articles:
        back_button_text = TRANSLATIONS["article_page"]["back_button"].get(lang, "Back")
        tags_html = ""
        if article.get('tags'):
            tags_html = '<div class="article-card-tags" style="margin-bottom: 20px;">'
            for tag in article['tags']:
                tags_html += f'<a href="/{lang}/index.html#{tag}" class="tag">{tag}</a>'
            tags_html += '</div>'
        
        article_view_html = f"""
        <div id="article-view">
            <a href="/{lang}/" class="back-button">{back_button_text}</a>
            {tags_html}
            {article['html_content']}
            <div class="footer-back-button" style="margin-top: 20px;">
                {tags_html}
                <a href="/{lang}/" class="back-button" style="margin-top: 20px;">{back_button_text}</a>
            </div>
        </div>
        """
        
        page_html = base_template.replace("{{content}}", article_view_html).replace("{{pagination_controls}}", "")
        # Replace other placeholders
        for key, value in TRANSLATIONS.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    page_html = page_html.replace(f"{{{{{key}_{sub_key}}}}}", sub_value.get(lang, sub_value.get("it", "")))
        
        lang_links = get_language_links()
        for link_placeholder, link_url in lang_links.items():
            page_html = page_html.replace(f"{{{{{link_placeholder}}}}}", link_url)
        page_html = page_html.replace("{{home_link}}", f"/{lang}/")
        page_html = page_html.replace("{{logo_path}}", "/logo_vn_ia.png")
        
        with open(os.path.join(output_dir, article['path']), "w") as f:
            f.write(page_html)

def generate_index_page(articles, output_dir, lang='it'):
    print("\nGenerating index pages...")
    with open("templates/base.html", "r") as f:
        base_template = f.read()
    
    try:
        locale.setlocale(locale.LC_TIME, f"{lang}_{lang.upper()}.UTF-8" if lang != 'en' else 'en_US.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, '')

    all_tags = sorted(list(set(tag for article in articles for tag in article.get('tags', []))))
    filter_bar_html = '<div id="tag-filter-bar" style="margin-bottom: 20px; text-align: center; flex-wrap: wrap; display: flex; justify-content: center; gap: 10px;">'
    filter_bar_html += '<button class="tag-filter-button active" data-tag="all">All</button>'
    for tag in all_tags:
        filter_bar_html += f'<button class="tag-filter-button" data-tag="{tag}">{tag}</button>'
    filter_bar_html += '</div>'

    ARTICLES_PER_PAGE = 15
    total_pages = math.ceil(len(articles) / ARTICLES_PER_PAGE)

    for page_num in range(1, total_pages + 1):
        start_index = (page_num - 1) * ARTICLES_PER_PAGE
        page_articles = articles[start_index:end_index]
        grid_html = '<div id="articles-grid">\n'
        for article in page_articles:
            date_html = f'<p class="article-card-date">{article["date"].strftime("%d %B %Y")}</p>' if article.get("date") else ""
            tags_html = '<div class="article-card-tags">' + "".join(f'<span class="tag">{tag}</span>' for tag in article.get("tags", [])) + '</div>' if article.get("tags") else ""
            tags_data_attr = " ".join(article.get('tags', []))
            card_html = f"""
            <a href="/{lang}/{article['path']}" class="article-card" data-tags="{tags_data_attr}">
                <img src="{article['image_url'] or '/logo_vn_ia.png'}" alt="{article['title']}" loading="lazy">
                <div class="article-card-content">{date_html}<h3>{article['title']}</h3><p>{article['summary']}</p>{tags_html}</div>
            </a>
            """
            grid_html += card_html
        grid_html += '</div>'

        pagination_html = ''
        if page_num > 1:
            prev_path = f"/page/{page_num - 1}/" if page_num > 2 else "/"
            pagination_html += f'<a href="/{lang}{prev_path}" class="prev-button">{TRANSLATIONS["pagination"]["prev"].get(lang, "")}</a>'
        if page_num < total_pages:
            next_path = f"/page/{page_num + 1}/"
            spacer = '<div style="flex-grow: 1;"></div>' if page_num > 1 else ''
            pagination_html += f'{spacer}<a href="/{lang}{next_path}" class="next-button">{TRANSLATIONS["pagination"]["next"].get(lang, "")}</a>'
        
        content_with_filter = filter_bar_html + grid_html if page_num == 1 else grid_html
        
        temp_html = base_template.replace("{{content}}", content_with_filter).replace("{{pagination_controls}}", pagination_html)
        for key, value in TRANSLATIONS.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    temp_html = temp_html.replace(f"{{{{{key}_{sub_key}}}}}", sub_value.get(lang, sub_value.get("it", "")))
        
        lang_links = get_language_links()
        for link_placeholder, link_url in lang_links.items():
            temp_html = temp_html.replace(f"{{{{{link_placeholder}}}}}", link_url)
        temp_html = temp_html.replace("{{home_link}}", f"/{lang}/")
        temp_html = temp_html.replace("{{logo_path}}", "/logo_vn_ia.png")

        output_path = os.path.join(output_dir, "index.html") if page_num == 1 else os.path.join(output_dir, "page", str(page_num), "index.html")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(temp_html)

def generate_local_pages(output_dir, lang='it'):
    print("\nGenerating local pages...")
    pages_dir = "pages"
    if not os.path.exists(pages_dir): return
    with open("templates/base.html", "r") as f:
        base_template = f.read()
    for filename in os.listdir(pages_dir):
        if filename.endswith(".html"):
            with open(os.path.join(pages_dir, filename), "r") as f:
                page_content = f.read()
            page_html = base_template.replace("{{content}}", page_content).replace("{{pagination_controls}}", "")
            # Replace other placeholders
            for key, value in TRANSLATIONS.items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        page_html = page_html.replace(f"{{{{{key}_{sub_key}}}}}", sub_value.get(lang, sub_value.get("it", "")))
            lang_links = get_language_links()
            for link_placeholder, link_url in lang_links.items():
                page_html = page_html.replace(f"{{{{{link_placeholder}}}}}", link_url)
            page_html = page_html.replace("{{home_link}}", f"/{lang}/")
            page_html = page_html.replace("{{logo_path}}", "/logo_vn_ia.png")
            with open(os.path.join(output_dir, filename), "w") as f:
                f.write(page_html)

def create_main_redirect():
    print("\nCreating root redirect...")
    html_content = """
<!DOCTYPE html><html><head><title>Notizie IA</title><meta http-equiv="refresh" content="0; url=/it/" /></head>
<body><p>Redirecting... <a href="/it/">Click here</a>.</p></body></html>
"""
    with open(os.path.join(BASE_OUTPUT_DIR, "index.html"), "w") as f:
        f.write(html_content)

def main():
    parser = argparse.ArgumentParser(description="Build the static site for a specific language.")
    parser.add_argument('--lang', default=None, help='Language to build (e.g., en, es). If not provided, all languages will be built.')
    args = parser.parse_args()

    if args.lang:
        langs_to_build = [args.lang]
    else:
        langs_to_build = LANGUAGES

    all_files = get_all_repo_files()
    if not all_files: return
    articles_db = structure_articles_by_language(all_files)

    for lang in langs_to_build:
        output_dir = os.path.join(BASE_OUTPUT_DIR, lang)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        md_files = get_files_for_lang(articles_db, lang)
        processed_articles = [p for p in (process_article(md) for md in md_files) if p]
        
        # This sort is now correct because None dates are handled by process_article
        # But user wants original sorting, so we leave it untouched.
        # The original sorting is based on filename and happens in main() before this loop.
        # Oops, the sorting was removed. I need to re-add the original sorting logic.

        # I will re-add the original sorting here.
        s1 = sorted(md_files, key=lambda x: x['name'].lower(), reverse=True)
        sorted_md_files = sorted(s1, key=lambda x: x['parent_dir'], reverse=True)
        
        processed_articles = []
        for md_file in sorted_md_files:
             article_data = process_article(md_file)
             if article_data:
                processed_articles.append(article_data)

        generate_article_pages(processed_articles, output_dir, lang)
        generate_index_page(processed_articles, output_dir, lang)
        generate_local_pages(output_dir, lang)
        # generate_rss_feed(processed_articles, output_dir, lang) # Assuming RSS is per-language

    if not args.lang:
        create_main_redirect()

if __name__ == "__main__":
    main()
