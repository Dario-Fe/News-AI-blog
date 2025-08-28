import os
import requests
import frontmatter
import shutil
import argparse
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
import markdown2
import math
from urllib.parse import quote, urlparse
import locale
import json
from PIL import Image
import hashlib
from io import BytesIO

# Constants
GITHUB_API_URL = "https://api.github.com/repos/matteobaccan/CorsoAIBook/contents/articoli"
SITE_URL = "https://aitalk.it/"
BASE_OUTPUT_DIR = "dist"
IMAGE_ASSETS_DIR = "assets/images"

# --- Image Processing Helpers ---

def process_and_save_image(image_url, output_dir_base, lang):
    """
    Downloads an image, creates two sizes (thumbnail and full),
    saves them in WebP and JPEG formats, and returns their paths.
    """
    if not image_url:
        return None

    try:
        response = requests.get(image_url, timeout=15)
        response.raise_for_status()
        image_bytes = response.content
    except requests.exceptions.RequestException as e:
        print(f"  - WARN: Could not download image {image_url}. Error: {e}")
        return None

    try:
        # Create a unique filename based on the image URL to avoid collisions
        url_hash = hashlib.sha1(image_url.encode()).hexdigest()[:10]
        original_filename = os.path.splitext(os.path.basename(urlparse(image_url).path))[0]
        base_filename = f"{original_filename}-{url_hash}"

        img = Image.open(BytesIO(image_bytes))
        img = img.convert("RGB") # Convert to RGB to ensure JPEG saving works

        # Define output directory for this language's images
        output_dir_images = os.path.join(output_dir_base, lang, IMAGE_ASSETS_DIR)
        if not os.path.exists(output_dir_images):
            os.makedirs(output_dir_images)

        image_paths = {}

        # --- Process Thumbnail (for cards) ---
        thumb_filename_webp = f"{base_filename}-thumb.webp"
        thumb_filename_jpeg = f"{base_filename}-thumb.jpeg"
        
        thumb = img.copy()
        thumb.thumbnail((400, 400)) # Resize to 400px width, maintaining aspect ratio
        
        thumb_path_webp = os.path.join(output_dir_images, thumb_filename_webp)
        thumb.save(thumb_path_webp, "webp", quality=80)
        
        thumb_path_jpeg = os.path.join(output_dir_images, thumb_filename_jpeg)
        thumb.save(thumb_path_jpeg, "jpeg", quality=80)
        
        image_paths['thumb_webp'] = f"{IMAGE_ASSETS_DIR}/{thumb_filename_webp}"
        image_paths['thumb_jpeg'] = f"{IMAGE_ASSETS_DIR}/{thumb_filename_jpeg}"
        
        # --- Process Full Size (for articles) ---
        full_filename_webp = f"{base_filename}-full.webp"
        full_filename_jpeg = f"{base_filename}-full.jpeg"

        full = img.copy()
        # The 'full' version is no longer resized to preserve original dimensions
        # if full.width > 800:
        #     full.thumbnail((800, 800)) # Resize to 800px width if it's larger
        
        full.save(os.path.join(output_dir_images, full_filename_webp), "webp", quality=85)
        full.save(os.path.join(output_dir_images, full_filename_jpeg), "jpeg", quality=85)

        image_paths['full_webp'] = f"{IMAGE_ASSETS_DIR}/{full_filename_webp}"
        image_paths['full_jpeg'] = f"{IMAGE_ASSETS_DIR}/{full_filename_jpeg}"
        
        return image_paths

    except Exception as e:
        print(f"  - WARN: Could not process image {image_url}. Error: {e}")
        return None

# Translations
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
            "es": "Suscríbete a nuestro boletín",
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
        },
        "consent_label": {
            "it": "Dichiaro di aver letto e accetto la <a href=\"privacy.html\" target=\"_blank\">Privacy Policy</a>.",
            "en": "I declare that I have read and accept the <a href=\"privacy.html\" target=\"_blank\">Privacy Policy</a>.",
            "es": "Declaro que he leído y acepto la <a href=\"privacy.html\" target=\"_blank\">Política de Privacidad</a>.",
            "fr": "Je déclare avoir lu et accepté la <a href=\"privacy.html\" target=\"_blank\">Politique de Confidentialité</a>.",
            "de": "Ich erkläre, dass ich die <a href=\"privacy.html\" target=\"_blank\">Datenschutzrichtlinie</a> gelesen habe und akzeptiere."
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
        },
        "view_more": {
            "it": "Carica Altri Articoli",
            "en": "Load More Articles",
            "es": "Cargar más artículos",
            "fr": "Charger plus d'articles",
            "de": "Weitere Artikel laden"
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
    },
    "cookie_page": {
        "title": {
            "it": "La nostra No Cookie Policy",
            "en": "Our No Cookie Policy",
            "es": "Nuestra política de no cookies",
            "fr": "Notre politique de non-utilisation de cookies",
            "de": "Unsere Keine-Cookies-Richtlinie"
        },
        "p1": {
            "it": "Ci asteniamo volutamente dall'usare cookie di qualsiasi genere: di tracciamento, marketing o tecnici.",
            "en": "We deliberately refrain from using cookies of any kind: tracking, marketing, or technical.",
            "es": "Nos abstenemos deliberadamente de utilizar cookies de cualquier tipo: de seguimiento, de marketing o técnicas.",
            "fr": "Nous nous abstenons délibérément d'utiliser des cookies de quelque nature que ce soit : de suivi, de marketing ou techniques.",
            "de": "Wir verzichten bewusst auf den Einsatz von Cookies jeglicher Art: Tracking-, Marketing- oder technische Cookies."
        },
        "p2": {
            "it": "Per questo aderiamo alla \"No Cookie Policy\": non serve raccogliere dei cookie per dare un buon servizio.",
            "en": "This is why we adhere to the \"No Cookie Policy\": it is not necessary to collect cookies to provide a good service.",
            "es": "Por eso nos adherimos a la \"Política de no cookies\": no es necesario recopilar cookies para dar un buen servicio.",
            "fr": "C'est pourquoi nous adhérons à la « No Cookie Policy » : il n'est pas nécessaire de collecter des cookies pour fournir un bon service.",
            "de": "Deshalb halten wir uns an die „Keine-Cookies-Richtlinie“: Es ist nicht notwendig, Cookies zu sammeln, um einen guten Service zu bieten."
        },
        "p3": {
            "it": "Per questa ragione la tua visita al nostro sito web non viene monitorata in nessun modo.",
            "en": "For this reason, your visit to our website is not monitored in any way.",
            "es": "Por esta razón, su visita a nuestro sitio web no es monitoreada de ninguna manera.",
            "fr": "Pour cette raison, votre visite sur notre site web n'est en aucun cas surveillée.",
            "de": "Aus diesem Grund wird Ihr Besuch auf unserer Website in keiner Weise überwacht."
        },
        "p4": {
            "it": "Riportiamo dal sito del Garante della Privacy la definizione di cookie.",
            "en": "We report the definition of cookies from the Privacy Guarantor's website.",
            "es": "Reportamos la definición de cookies del sitio web del Garante de la Privacidad.",
            "fr": "Nous rapportons la définition des cookies du site de l'Autorité de protection de la vie privée.",
            "de": "Wir berichten über die Definition von Cookies von der Website der Datenschutzbehörde."
        },
        "quote": {
            "it": "I cookie sono stringhe di testo che i siti web visitati dagli utenti (cd. Publisher, o \"prime parti\") ovvero siti o web server diversi (cd. \"terze parti\") posizionano ed archiviano all'interno del dispositivo terminale dell'utente medesimo, perché siano poi ritrasmessi agli stessi siti alla visita successiva.",
            "en": "Cookies are text strings that websites visited by users (so-called Publishers, or \"first parties\") or different sites or web servers (so-called \"third parties\") place and store within the user's terminal device, to be then retransmitted to the same sites on the next visit.",
            "es": "Las cookies son cadenas de texto que los sitios web visitados por los usuarios (los llamados Editores, o \"primeras partes\") o diferentes sitios o servidores web (los llamados \"terceras partes\") colocan y almacenan en el dispositivo terminal del usuario, para ser luego retransmitidas a los mismos sitios en la siguiente visita.",
            "fr": "Les cookies sont des chaînes de texte que les sites web visités par les utilisateurs (appelés Éditeurs, ou « premières parties ») ou des sites ou serveurs web différents (appelés « tierces parties ») placent et stockent dans le terminal de l'utilisateur, pour être ensuite retransmis aux mêmes sites lors d'une visite ultérieure.",
            "de": "Cookies sind Textzeichenfolgen, die von den von den Benutzern besuchten Websites (sog. Publisher oder „Erstanbieter“) oder verschiedenen Websites oder Webservern (sog. „Drittanbieter“) auf dem Endgerät des Benutzers platziert und gespeichert werden, um dann bei einem späteren Besuch an dieselben Websites zurückgesendet zu werden."
        },
        "p5": {
            "it": "Esiste un solo modo in cui possiamo sapere se hai visitato il nostro sito: se ci contatti per conoscerci.",
            "en": "There is only one way we can know if you have visited our site: if you contact us to get to know us.",
            "es": "Solo hay una forma de saber si ha visitado nuestro sitio: si se pone en contacto con nosotros para conocernos.",
            "fr": "Il n'y a qu'une seule façon pour nous de savoir si vous avez visité notre site : si vous nous contactez pour faire connaissance.",
            "de": "Es gibt nur eine Möglichkeit, wie wir wissen können, ob Sie unsere Seite besucht haben: wenn Sie uns kontaktieren, um uns kennenzulernen."
        },
        "link_text": {
            "it": "Verifica l'assenza di cookie dal nostro sito",
            "en": "Verify the absence of cookies from our site",
            "es": "Verifique la ausencia de cookies en nuestro sitio",
            "fr": "Vérifiez l'absence de cookies sur notre site",
            "de": "Überprüfen Sie das Nichtvorhandensein von Cookies auf unserer Website"
        },
        "link_url": {
            "it": "https://www.cookieserve.com/it/scan-summary/?url=https%3A%2F%2Fianotizie.netlify.app%2Fit%2F",
            "en": "https://www.cookieserve.com/scan-summary/?url=https%3A%2F%2Fianotizie.netlify.app%2Fen%2F",
            "es": "https://www.cookieserve.com/es/scan-summary/?url=https%3A%2F%2Fianotizie.netlify.app%2Fes%2F",
            "fr": "https://www.cookieserve.com/fr/scan-summary/?url=https%3A%2F%2Fianotizie.netlify.app%2Ffr%2F",
            "de": "https://www.cookieserve.com/de/scan-summary/?url=https%3A%2F%2Fianotizie.netlify.app%2Fde%2F"
        }
    },
    "privacy_page": {
        "title": {
            "it": "Privacy Policy",
            "en": "Privacy Policy",
            "es": "Política de privacidad",
            "fr": "Politique de confidentialité",
            "de": "Datenschutz-Bestimmungen"
        },
        "p1": {
            "it": "Questo sito non raccoglie dati personali di alcun tipo, ad eccezione del nome e dell'indirizzo email forniti volontariamente dagli utenti che si iscrivono alla nostra newsletter. Il nostro obiettivo non è raccogliere informazioni su di voi, ma condividere la passione per l'intelligenza artificiale e il mondo tech.",
            "en": "This site does not collect personal data of any kind, except for the name and email address voluntarily provided by users who subscribe to our newsletter. Our goal is not to collect information about you, but to share the passion for artificial intelligence and the tech world.",
            "es": "Este sitio no recopila datos personales de ningún tipo, a excepción del nombre y la dirección de correo electrónico proporcionados voluntariamente por los usuarios que se suscriben a nuestro boletín. Nuestro objetivo no es recopilar información sobre usted, sino compartir la pasión por la inteligencia artificial y el mundo de la tecnología.",
            "fr": "Ce site ne collecte aucune donnée personnelle, à l'exception du nom et de l'adresse e-mail fournis volontariamente par les utilisateurs qui s'abonnent à notre newsletter. Notre objectif n'est pas de collecter des informations sur vous, mais de partager la passion pour l'intelligence artificielle et le monde de la technologie.",
            "de": "Diese Website sammelt keinerlei personenbezogene Daten, mit Ausnahme des Namens und der E-Mail-Adresse, die von Benutzern, die unseren Newsletter abonnieren, freiwillig angegeben werden. Unser Ziel ist es nicht, Informationen über Sie zu sammeln, sondern die Leidenschaft für künstliche Intelligenz und die Tech-Welt zu teilen."
        },
        "p2": {
            "it": "I dati forniti (nome ed email) vengono utilizzati esclusivamente per inviarti aggiornamenti, articoli e novità tramite la nostra newsletter. Non condivideremo mai queste informazioni con terze parti senza il tuo esplicito consenso.",
            "en": "The data provided (name and email) are used exclusively to send you updates, articles, and news through our newsletter. We will never share this information with third parties without your explicit consent.",
            "es": "Los datos proporcionados (nombre y correo electrónico) se utilizan exclusivamente para enviarle actualizaciones, artículos y noticias a través de nuestro boletín. Nunca compartiremos esta información con terceros sin su consentimiento explícito.",
            "fr": "Les données fournies (nom et e-mail) sont utilisées exclusivamente pour vous envoyer des mises à jour, des articles et des nouvelles via notre newsletter. Nous ne partagerons jamais ces informations avec des tiers sans votre consentement explicite.",
            "de": "Die angegebenen Daten (Name und E-Mail) werden ausschließlich dazu verwendet, Ihnen über unseren Newsletter Updates, Artikel und Neuigkeiten zuzusenden. Wir werden diese Informationen niemals ohne Ihre ausdrückliche Zustimmung an Dritte weitergeben."
        },
        "p3_1": {
            "it": "Il sito è ospitato su Netlify, che potrebbe raccogliere dati anonimi per scopi tecnici, come la protezione da attività dannose e la manutenzione del servizio. Per maggiori dettagli, puoi consultare l'",
            "en": "The site is hosted on Netlify, which may collect anonymous data for technical purposes, such as protection against malicious activities and service maintenance. For more details, you can consult Netlify's ",
            "es": "El sitio está alojado en Netlify, que puede recopilar datos anónimos con fines técnicos, como la protección contra actividades maliciosas y el mantenimiento del servicio. Para más detalles, puede consultar la ",
            "fr": "Le site est hébergé sur Netlify, qui peut collecter des données anonymes à des fins techniques, telles que la protection contre les activités malveillantes et la maintenance du service. Pour plus de détails, vous pouvez consulter la ",
            "de": "Die Website wird auf Netlify gehostet, das möglicherweise anonyme Daten für technische Zwecke sammelt, wie z. B. zum Schutz vor böswilligen Aktivitäten und zur Wartung des Dienstes. Weitere Informationen finden Sie in der "
        },
        "p3_link_text": {
            "it": "Informativa sulla privacy di Netlify",
            "en": "Netlify Privacy Policy",
            "es": "Política de privacidad de Netlify",
            "fr": "Politique de confidentialité de Netlify",
            "de": "Datenschutzrichtlinie von Netlify"
        },
        "p4": {
            "it": "Se desideri modificare, cancellare i tuoi dati o smettere di ricevere la newsletter, puoi contattarci in qualsiasi momento o utilizzare il link di cancellazione presente in ogni email.",
            "en": "If you wish to modify, delete your data, or stop receiving the newsletter, you can contact us at any time or use the unsubscribe link present in every email.",
            "es": "Si desea modificar, eliminar sus datos o dejar de recibir el boletín, puede contactarnos en cualquier momento o utilizar el enlace para cancelar la suscripción presente en cada correo electrónico.",
            "fr": "Si vous souhaitez modifier, supprimer vos données ou ne plus recevoir la newsletter, vous pouvez nous contacter à tout momento ou utiliser le lien de désinscription présent dans chaque e-mail.",
            "de": "Wenn Sie Ihre Daten ändern, löschen oder den Newsletter abbestellen möchten, können Sie uns jederzeit kontaktieren oder den in jeder E-Mail enthaltenen Abmeldelink verwenden."
        }
    },
    "not_found_page": {
        "title": {
            "it": "Pagina Non Trovata",
            "en": "Page Not Found",
            "es": "Página no encontrada",
            "fr": "Page non trouvée",
            "de": "Seite nicht gefunden"
        },
        "heading": {
            "it": "Oops! Pagina non trovata.",
            "en": "Oops! Page not found.",
            "es": "¡Vaya! Página no encontrada.",
            "fr": "Oups! Page non trouvée.",
            "de": "Hoppla! Seite nicht gefunden."
        },
        "paragraph": {
            "it": "La pagina che stai cercando potrebbe essere stata rimossa, rinominata o non essere mai esistita.",
            "en": "The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.",
            "es": "La página que busca podría haber sido eliminada, haber cambiado de nombre o no estar disponible temporalmente.",
            "fr": "La page que vous recherchez a peut-être été supprimée, renommée ou est temporairement indisponible.",
            "de": "Die von Ihnen gesuchte Seite wurde möglicherweise entfernt, umbenannt oder ist vorübergehend nicht verfügbar."
        },
        "button_text": {
            "it": "Torna alla Home",
            "en": "Back to Home",
            "es": "Volver al Inicio",
            "fr": "Retour à l'accueil",
            "de": "Zurück zur Startseite"
        }
    }
}

# It's recommended to use a GitHub token to avoid rate limiting.
# Create a Personal Access Token (PAT) with 'repo' scope and set it as an environment variable.
# For local development: export GITHUB_TOKEN='your_token_here'
# In GitHub Actions, this can be set as a secret.
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

LANGUAGES = ["it", "en", "es", "fr", "de"]

def get_language_links(depth):
    """
    Generates a dictionary of relative language links based on page depth.
    """
    links = {}
    path_prefix = "../" * depth
    for lang in LANGUAGES:
        links[f"{lang}_link"] = f"{path_prefix}{lang}/index.html"
    return links

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
                elif filename.endswith('_fr.md'):
                    lang = 'fr'
                elif filename.endswith('_de.md'):
                    lang = 'de'
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
    Can also be used to generate master files like sitemap and robots.txt.
    """
    parser = argparse.ArgumentParser(description="Build the static site for a specific language.")
    parser.add_argument('--lang', default=None, help='Language to build (e.g., en, es)')
    parser.add_argument('--master-files', action='store_true', help='Generate only the master files (sitemap.xml, robots.txt).')
    args = parser.parse_args()

    if args.master_files:
        generate_sitemap_xml()
        generate_robots_txt()
        create_root_redirect() # This is also a master file
        return

    lang = args.lang
    if not lang:
        print("Error: --lang is required unless generating master files with --master-files.")
        return
    output_dir = os.path.join(BASE_OUTPUT_DIR, lang)

    print(f"Starting build process for language: '{lang}'...")

    # Create language-specific output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create assets directory for images
    image_dir = os.path.join(output_dir, IMAGE_ASSETS_DIR)
    os.makedirs(image_dir, exist_ok=True)

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
        article_data = process_article(md_file, BASE_OUTPUT_DIR, lang)
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

    # 8. Generate 404 page
    generate_404_page(output_dir, lang)

    # 9. Copy static assets
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
    with open(os.path.join(BASE_OUTPUT_DIR, "index.html"), "w", encoding='utf-8') as f:
        f.write(html_content)
    print("  - dist/index.html (redirect)")


def process_article(md_file, output_dir_base, lang):
    """
    Fetches markdown, processes it, optimizes all images, and returns a dict.
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
        all_paragraphs = soup.find_all('p')
        for p in all_paragraphs:
            if p.get_text(strip=True) and not p.find('img'):
                summary = p.get_text()
                break

        # Process all images within the article body
        for img in soup.find_all('img'):
            original_src = img.get('src')
            if not original_src:
                continue

            # Make image src absolute before downloading
            if not original_src.startswith('http'):
                absolute_src = f"https://raw.githubusercontent.com/matteobaccan/CorsoAIBook/main/articoli/{md_file['parent_dir']}/{original_src}"
            else:
                absolute_src = original_src

            # Download, resize, and save the image
            processed_paths = process_and_save_image(absolute_src, output_dir_base, lang)

            if processed_paths:
                # Create a <picture> tag to replace the <img> tag
                picture_tag = soup.new_tag("picture")
                
                source_webp = soup.new_tag("source", attrs={"srcset": processed_paths['full_webp'], "type": "image/webp"})
                source_jpeg = soup.new_tag("source", attrs={"srcset": processed_paths['full_jpeg'], "type": "image/jpeg"})
                
                # Create a new fallback <img> tag
                fallback_img = soup.new_tag("img", attrs={
                    "src": processed_paths['full_jpeg'],
                    "alt": img.get('alt', 'Article image'),
                    "loading": "lazy"
                })

                picture_tag.append(source_webp)
                picture_tag.append(source_jpeg)
                picture_tag.append(fallback_img)
                
                # Replace the original img tag with the new picture tag
                img.replace_with(picture_tag)

        # Get the first image for the summary card (after processing)
        # We need to find the *original* first image URL for this.
        # Re-parsing the original content is one way.
        temp_soup = BeautifulSoup(markdown2.markdown(post.content), 'html.parser')
        first_img_tag = temp_soup.find('img')
        main_image_url = None
        if first_img_tag and first_img_tag.get('src'):
            src = first_img_tag['src']
            if not src.startswith('http'):
                main_image_url = f"https://raw.githubusercontent.com/matteobaccan/CorsoAIBook/main/articoli/{md_file['parent_dir']}/{src}"
            else:
                main_image_url = src
        
        main_image_paths = process_and_save_image(main_image_url, output_dir_base, lang)

        final_html_content = str(soup)
        slug = os.path.splitext(md_file['name'])[0].strip().replace('_', '-')
        tags = post.metadata.get('tags', [])
        date_obj = post.metadata.get('date', None)

        return {
            "title": title,
            "summary": summary,
            "image_paths": main_image_paths, # New field for optimized paths
            "html_content": final_html_content,
            "slug": slug,
            "path": f"{slug}.html",
            "tags": tags,
            "date": date_obj,
            "image_url": main_image_url # Keep original for RSS feed
        }

    except Exception as e:
        print(f"  Error parsing markdown for {md_file['name']}: {e}")
        return None

def generate_article_pages(articles, output_dir, lang='it'):
    """
    Generates an HTML page for each article.
    """
    print("\nGenerating article pages...")
    with open("templates/base.html", "r", encoding='utf-8') as f:
        base_template = f.read()

    for article in articles:
        print(f"  - {article['path']}")

        # Get translation for the back button
        back_button_text = TRANSLATIONS["article_page"]["back_button"].get(lang, TRANSLATIONS["article_page"]["back_button"]["it"])

        # --- Tags Formatting ---
        tags_html = ""
        if article.get('tags'):
            tags_html = '<div class="article-card-tags" style="margin-bottom: 20px;">'
            for tag in article['tags']:
                # The link will point to the homepage with a hash for the JS to pick up
                tags_html += f'<a href="index.html#{tag}" class="tag">{tag}</a>'
            tags_html += '</div>'

        # Create a simple view for the article content
        article_view_html = f"""
        <div id="article-view">
            <a href="index.html" class="back-button">{back_button_text}</a>
            {tags_html}
            {article['html_content']}
            <div class="footer-back-button">
                {tags_html}
                <a href="index.html" class="back-button" style="margin-top: 20px;">{back_button_text}</a>
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
        lang_links = get_language_links(depth=1)

        temp_html = base_template.replace("{{subtitle}}", subtitle)
        temp_html = temp_html.replace("{{subscribe_link_text}}", subscribe_text)
        temp_html = temp_html.replace("{{footer_curated_by}}", footer_curated_by)
        temp_html = temp_html.replace("{{footer_contacts}}", footer_contacts)
        temp_html = temp_html.replace("{{home_link}}", home_link)
        temp_html = temp_html.replace("{{logo_path}}", logo_path)
        temp_html = temp_html.replace("{{pagination_controls}}", "") # No pagination on article pages

        # SEO
        page_title = f"{article['title']} - AITalk"
        meta_description = article['summary']
        temp_html = temp_html.replace("{{page_title}}", page_title)
        temp_html = temp_html.replace("{{meta_description}}", meta_description)

        # Replace language links
        for link_placeholder, link_url in lang_links.items():
            temp_html = temp_html.replace(f"{{{{{link_placeholder}}}}}", link_url)

        final_page_html = temp_html.replace("{{content}}", article_view_html)

        with open(os.path.join(output_dir, article['path']), "w", encoding='utf-8') as f:
            f.write(final_page_html)

def generate_index_page(articles, output_dir, lang='it'):
    """
    Generates the index page with the first batch of articles and a JSON
    file for the rest to be loaded dynamically.
    """
    print("\nGenerating index page and JSON for dynamic loading...")
    with open("templates/base.html", "r", encoding='utf-8') as f:
        base_template = f.read()

    # Set locale for date formatting
    try:
        if lang == 'it':
            locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')
        elif lang == 'en':
            locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        elif lang == 'es':
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        elif lang == 'fr':
            locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        elif lang == 'de':
            locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
    except locale.Error:
        print(f"Locale for {lang} not supported, using default.")
        locale.setlocale(locale.LC_TIME, '')

    # --- Create Tag Filter Bar ---
    all_tags = sorted(list(set(tag for article in articles for tag in article.get('tags', []))))
    filter_bar_html = '<div id="tag-filter-bar" style="margin-bottom: 20px; text-align: center; flex-wrap: wrap; display: flex; justify-content: center; gap: 10px;">'
    filter_bar_html += '<button class="tag-filter-button active" data-tag="all">All</button>'
    for tag in all_tags:
        filter_bar_html += f'<button class="tag-filter-button" data-tag="{tag}">{tag}</button>'
    filter_bar_html += '</div>'

    ARTICLES_PER_PAGE = 15
    initial_articles = articles[:ARTICLES_PER_PAGE]
    all_articles_for_json = articles # All articles go into the JSON

    # --- Generate HTML for the first page articles ---
    grid_html = '<div id="articles-grid">\n'
    for article in initial_articles:
        date_html = ""
        if article.get('date'):
            formatted_date = article['date'].strftime('%d %B %Y')
            date_html = f'<p class="article-card-date">{formatted_date}</p>'

        tags_html = ""
        if article.get('tags'):
            tags_html = '<div class="article-card-tags">'
            for tag in article['tags']:
                tags_html += f'<span class="tag">{tag}</span>'
            tags_html += '</div>'
        
        image_html = ''
        if article.get('image_paths'):
            paths = article['image_paths']
            image_html = f"""
                <picture>
                    <source srcset="{paths['thumb_webp']}" type="image/webp">
                    <source srcset="{paths['thumb_jpeg']}" type="image/jpeg">
                    <img src="{paths['thumb_jpeg']}" alt="{article['title']}" loading="lazy">
                </picture>
            """
        else:
            image_html = f'<img src="logo_vn_ia.png" alt="{article["title"]}" loading="lazy">'

        tags_data_attr = " ".join(article.get('tags', []))

        card_html = f"""
            <a href="{article['path']}" class="article-card" data-tags="{tags_data_attr}">
                {image_html}
                <div class="article-card-content">
                    {date_html}
                    <h3>{article['title']}</h3>
                    <p>{article['summary']}</p>
                    {tags_html}
                </div>
            </a>
            """
        grid_html += card_html
    grid_html += '</div>'

    # --- Generate JSON for all articles ---
    json_output_path = os.path.join(output_dir, "articles.json")

    # Create a serializable version of all articles
    serializable_articles = []
    for article in all_articles_for_json:
        article_copy = article.copy()
        if 'date' in article_copy and article_copy['date'] is not None:
            article_copy['date'] = article_copy['date'].isoformat()
        else:
            article_copy['date'] = None
        serializable_articles.append(article_copy)

    with open(json_output_path, "w", encoding='utf-8') as f:
        json.dump(serializable_articles, f, ensure_ascii=False)
    print(f"  - Generated articles.json with {len(all_articles_for_json)} articles.")


    # --- Pagination Controls (will be a "View More" button handled by JS) ---
    pagination_html = ''
    # The button is shown if there are more articles than initially displayed
    if len(articles) > ARTICLES_PER_PAGE:
        # The button itself will be added via JS in the template for easier translation.
        # We just need a container for it.
        pagination_html = '<div id="view-more-container"></div>'

    # --- Final HTML Generation for index.html ---
    subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
    subscribe_text = TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"])
    footer_curated_by = TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"])
    footer_contacts = TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"])

    # Paths and links for the root index.html
    home_link = "index.html"
    logo_path = "logo_vn_ia.png"
    lang_links = get_language_links(depth=1)
    content_with_filter = filter_bar_html + grid_html

    temp_html = base_template.replace("{{subtitle}}", subtitle)
    temp_html = temp_html.replace("{{subscribe_link_text}}", subscribe_text)
    temp_html = temp_html.replace("{{footer_curated_by}}", footer_curated_by)
    temp_html = temp_html.replace("{{footer_contacts}}", footer_contacts)
    temp_html = temp_html.replace("{{home_link}}", home_link)
    temp_html = temp_html.replace("{{logo_path}}", logo_path)
    temp_html = temp_html.replace("{{content}}", content_with_filter)
    temp_html = temp_html.replace("{{pagination_controls}}", pagination_html)

    # Add data for the 'View More' script
    view_more_text = TRANSLATIONS["pagination"]["view_more"].get(lang, TRANSLATIONS["pagination"]["view_more"]["it"])
    temp_html = temp_html.replace("{{lang}}", lang)
    temp_html = temp_html.replace("{{view_more_text}}", view_more_text.replace("'", "\\'"))

    # SEO
    page_title = f"AITalk - {subtitle}"
    meta_description = subtitle
    temp_html = temp_html.replace("{{page_title}}", page_title)
    temp_html = temp_html.replace("{{meta_description}}", meta_description)

    for link_placeholder, link_url in lang_links.items():
        temp_html = temp_html.replace(f"{{{{{link_placeholder}}}}}", link_url)

    output_path = os.path.join(output_dir, "index.html")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"  - Generating index.html at {output_path}")
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(temp_html)

def generate_local_pages(output_dir, lang='it'):
    """
    Generates standalone pages from the /pages directory.
    """
    # SEO Metadata for local pages
    local_pages_meta = {
        "newsletter.html": {
            "title": TRANSLATIONS["newsletter_page"]["title"].get(lang, TRANSLATIONS["newsletter_page"]["title"]["it"]),
            "description": TRANSLATIONS["newsletter_page"]["description"].get(lang, TRANSLATIONS["newsletter_page"]["description"]["it"])
        },
        "thank-you.html": {
            "title": TRANSLATIONS["thank_you_page"]["title"].get(lang, TRANSLATIONS["thank_you_page"]["title"]["it"]),
            "description": TRANSLATIONS["thank_you_page"]["paragraph"].get(lang, TRANSLATIONS["thank_you_page"]["paragraph"]["it"])
        },
        "cookie.html": {
            "title": TRANSLATIONS["cookie_page"]["title"].get(lang, TRANSLATIONS["cookie_page"]["title"]["it"]),
            "description": TRANSLATIONS["cookie_page"]["p1"].get(lang, TRANSLATIONS["cookie_page"]["p1"]["it"])
        },
        "privacy.html": {
            "title": TRANSLATIONS["privacy_page"]["title"].get(lang, TRANSLATIONS["privacy_page"]["title"]["it"]),
            "description": TRANSLATIONS["privacy_page"]["p1"].get(lang, TRANSLATIONS["privacy_page"]["p1"]["it"])
        }
    }
    print("\nGenerating local pages...")
    pages_dir = "pages"
    if not os.path.exists(pages_dir):
        return

    with open("templates/base.html", "r", encoding='utf-8') as f:
        base_template = f.read()

    for filename in os.listdir(pages_dir):
        if filename.endswith(".html"):
            print(f"  - {filename}")
            with open(os.path.join(pages_dir, filename), "r", encoding='utf-8') as f:
                page_content = f.read()

            # Replace placeholders in the base template
            subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
            subscribe_text = TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"])
            footer_curated_by = TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"])
            footer_contacts = TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"])

            # Path for pages at root level of language dir
            home_link = "index.html"
            logo_path = "logo_vn_ia.png"
            lang_links = get_language_links(depth=1)

            temp_html = base_template.replace("{{subtitle}}", subtitle)
            temp_html = temp_html.replace("{{subscribe_link_text}}", subscribe_text)
            temp_html = temp_html.replace("{{footer_curated_by}}", footer_curated_by)
            temp_html = temp_html.replace("{{footer_contacts}}", footer_contacts)
            temp_html = temp_html.replace("{{home_link}}", home_link)
            temp_html = temp_html.replace("{{logo_path}}", logo_path)
            temp_html = temp_html.replace("{{pagination_controls}}", "") # No pagination on local pages

            # SEO
            meta_info = local_pages_meta.get(filename, {"title": "AITalk", "description": subtitle})
            page_title = f"{meta_info['title']} - AITalk"
            meta_description = meta_info['description']
            temp_html = temp_html.replace("{{page_title}}", page_title)
            temp_html = temp_html.replace("{{meta_description}}", meta_description)

            # Replace language links
            for link_placeholder, link_url in lang_links.items():
                temp_html = temp_html.replace(f"{{{{{link_placeholder}}}}}", link_url)

            # Replace placeholders in the page content itself
            final_content = page_content
            if filename == "newsletter.html":
                for key, trans_dict in TRANSLATIONS["newsletter_page"].items():
                    placeholder = f"{{{{newsletter_page_{key}}}}}"
                    translation = trans_dict.get(lang, trans_dict["it"])
                    final_content = final_content.replace(placeholder, translation)

            if filename == "thank-you.html":
                for key, trans_dict in TRANSLATIONS["thank_you_page"].items():
                    placeholder = f"{{{{thank_you_page_{key}}}}}"
                    translation = trans_dict.get(lang, trans_dict["it"])
                    final_content = final_content.replace(placeholder, translation)

            if filename == "cookie.html":
                for key, trans_dict in TRANSLATIONS["cookie_page"].items():
                    placeholder = f"{{{{cookie_page_{key}}}}}"
                    translation = trans_dict.get(lang, trans_dict["it"])
                    final_content = final_content.replace(placeholder, translation)

            if filename == "privacy.html":
                for key, trans_dict in TRANSLATIONS["privacy_page"].items():
                    placeholder = f"{{{{privacy_page_{key}}}}}"
                    translation = trans_dict.get(lang, trans_dict["it"])
                    final_content = final_content.replace(placeholder, translation)

            # Inject the dynamic, absolute thank you page link
            thank_you_link = f"/{lang}/thank-you.html"
            final_content = final_content.replace("{{thank_you_link}}", thank_you_link)

            # For any page with a newsletter form, update its name and add hidden lang field
            soup = BeautifulSoup(final_content, 'html.parser')
            form = soup.find('form', {'name': 'newsletter'})
            if form:
                form_name = f"newsletter-{lang}"
                form['name'] = form_name

                # Add hidden form-name input for Netlify
                form_name_input = soup.new_tag('input', attrs={'type': 'hidden', 'name': 'form-name', 'value': form_name})
                form.append(form_name_input)

                # Add language input only if it's the main newsletter form
                if filename == "newsletter.html":
                    hidden_input = soup.new_tag('input', attrs={'type': 'hidden', 'name': 'language', 'value': lang})
                    form.append(hidden_input)
                final_content = str(soup)

            final_page_html = temp_html.replace("{{content}}", final_content)

            with open(os.path.join(output_dir, filename), "w", encoding='utf-8') as f:
                f.write(final_page_html)

def generate_404_page(output_dir, lang='it'):
    """
    Generates a localized 404.html page.
    """
    print("\nGenerating 404 page...")
    with open("templates/base.html", "r", encoding='utf-8') as f:
        base_template = f.read()
    with open("templates/404.html", "r", encoding='utf-8') as f:
        page_content = f.read()

    # Replace placeholders in the base template
    subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
    subscribe_text = TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"])
    footer_curated_by = TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"])
    footer_contacts = TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"])
    
    # Path for pages at root level of language dir
    home_link = "index.html"
    logo_path = "logo_vn_ia.png" # This is now a fallback, but we keep the variable for consistency
    lang_links = get_language_links(depth=1)

    temp_html = base_template.replace("{{subtitle}}", subtitle)
    temp_html = temp_html.replace("{{subscribe_link_text}}", subscribe_text)
    temp_html = temp_html.replace("{{footer_curated_by}}", footer_curated_by)
    temp_html = temp_html.replace("{{footer_contacts}}", footer_contacts)
    temp_html = temp_html.replace("{{home_link}}", home_link)
    # The logo path is now hardcoded in the <picture> element in base.html, so this replace does nothing.
    temp_html = temp_html.replace("{{logo_path}}", logo_path) 
    temp_html = temp_html.replace("{{pagination_controls}}", "") # No pagination on 404 page

    # SEO for 404 page
    title = TRANSLATIONS["not_found_page"]["title"].get(lang, TRANSLATIONS["not_found_page"]["title"]["it"])
    page_title = f"{title} - AITalk"
    # A generic description for 404 page
    meta_description = TRANSLATIONS["not_found_page"]["paragraph"].get(lang, TRANSLATIONS["not_found_page"]["paragraph"]["it"])
    temp_html = temp_html.replace("{{page_title}}", page_title)
    temp_html = temp_html.replace("{{meta_description}}", meta_description)

    # Replace language links
    for link_placeholder, link_url in lang_links.items():
        temp_html = temp_html.replace(f"{{{{{link_placeholder}}}}}", link_url)

    # Replace placeholders in the 404 page content itself
    final_content = page_content
    for key, trans_dict in TRANSLATIONS["not_found_page"].items():
        placeholder = f"{{{{not_found_page_{key}}}}}"
        translation = trans_dict.get(lang, trans_dict["it"])
        final_content = final_content.replace(placeholder, translation)
    
    final_page_html = temp_html.replace("{{content}}", final_content)

    output_path = os.path.join(output_dir, "404.html")
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(final_page_html)
    print(f"  - {output_path}")


def copy_static_assets(output_dir):
    """
    Copies static assets from the root to the output directory.
    """
    print("\nCopying static assets...")
    static_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js', '.html', '.webp', '.ico']
    for item in os.listdir('.'):
        if os.path.isfile(item) and any(item.endswith(ext) for ext in static_extensions):
            # Let's avoid copying the template files themselves if they are in the root
            if item not in ["base.html", "forms.html"]: # Simple exclusion for templates
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

    for article in reversed(articles):
        fe = fg.add_entry()
        fe.title(article['title'])
        # URL encode the path to handle spaces and special characters
        encoded_path = quote(article['path'])
        fe.link(href=f"{SITE_URL}{lang}/{encoded_path}")
        fe.description(article['summary'])

        # Add the article image as an enclosure
        if article.get('image_url'):
            # It's better to assume the MIME type from the extension if possible,
            # but for now, we'll default to jpeg.
            # The length is often required, but many readers are lenient.
            # Setting to '0' is a common practice when the size is unknown.
            fe.enclosure(url=article['image_url'], length='0', type='image/jpeg')

        # fe.pubDate() # We could add pubDate if we can parse it from the article name or metadata

    fg.rss_file(os.path.join(output_dir, 'rss.xml'), pretty=True)
    print(f"  - rss.xml (for {lang})")

    print("Build process finished successfully!")


def generate_sitemap_xml():
    """
    Generates a sitemap.xml for all articles in all languages.
    This function is intended to be called once after all languages are built.
    """
    print("\nGenerating sitemap.xml...")

    all_files = get_all_repo_files()
    if not all_files:
        print("  Could not fetch files for sitemap generation.")
        return

    articles_db = structure_articles_by_language(all_files)

    urls = []
    # Add base URLs for each language's index page
    for lang in LANGUAGES:
        urls.append(f"{SITE_URL}{lang}/")

    # Add URLs for each article
    for article_dir, languages in articles_db.items():
        for lang, files in languages.items():
            for file_info in files:
                slug = os.path.splitext(file_info['name'])[0].strip()
                path = f"{slug}.html"
                # URL encode the path to handle spaces and special characters
                encoded_path = quote(path)
                urls.append(f"{SITE_URL}{lang}/{encoded_path}")

    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sorted(urls):
        xml_content += f"  <url>\n    <loc>{url}</loc>\n  </url>\n"
    xml_content += '</urlset>'

    sitemap_path = os.path.join(BASE_OUTPUT_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding='utf-8') as f:
        f.write(xml_content)

    print(f"  - sitemap.xml generated with {len(urls)} URLs.")


def generate_robots_txt():
    """
    Generates a robots.txt file in the output directory.
    """
    print("\nGenerating robots.txt...")
    content = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_URL}sitemap.xml"
    )
    robots_path = os.path.join(BASE_OUTPUT_DIR, "robots.txt")
    with open(robots_path, "w", encoding='utf-8') as f:
        f.write(content)
    print("  - robots.txt generated.")


if __name__ == "__main__":
    main()
