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
import re
from PIL import Image
import hashlib
from io import BytesIO
from datetime import datetime, date, timezone

# Constants
SITE_URL = "https://aitalk.it/"
BASE_OUTPUT_DIR = "dist"
ARTICLES_DIR = "articoli" # New constant for local articles path
IMAGE_ASSETS_DIR = "assets/images"
AUDIO_ASSETS_DIR = "assets/audio"

# --- Media Processing Helpers ---

def process_and_save_image(image_source, output_dir_base, lang, article_dir=""):
    """
    Downloads or copies an image, creates two sizes (thumbnail and full),
    saves them in WebP and JPEG formats, and returns their paths.
    'image_source' can be a URL or a local file path.
    """
    if not image_source:
        return None

    image_bytes = None
    source_filename = ""
    
    if image_source.startswith("http"):
        try:
            response = requests.get(image_source, timeout=15)
            response.raise_for_status()
            image_bytes = response.content
            source_filename = os.path.basename(urlparse(image_source).path)
        except requests.exceptions.RequestException as e:
            print(f"  - ERROR: Could not download image {image_source}. Error: {e}")
            raise  # Re-raise the exception to stop the build
    else: # It's a local file
        local_path = os.path.join(ARTICLES_DIR, article_dir, image_source)
        if os.path.exists(local_path):
            with open(local_path, "rb") as f:
                image_bytes = f.read()
            source_filename = os.path.basename(local_path)
        else:
            print(f"  - ERROR: Could not find local image {local_path}.")
            raise FileNotFoundError(f"Image not found at {local_path}")

    if not image_bytes:
        # This case should ideally not be reached if the above checks are correct, but as a safeguard:
        raise ValueError("Image processing failed: image_bytes is empty.")

    try:
        # Create a unique filename based on the content to avoid collisions and handle updates
        content_hash = hashlib.sha1(image_bytes).hexdigest()[:10]
        base_name, _ = os.path.splitext(source_filename)
        base_filename = f"{base_name}-{content_hash}"

        img = Image.open(BytesIO(image_bytes))
        img = img.convert("RGB")

        output_dir_images = os.path.join(output_dir_base, lang, IMAGE_ASSETS_DIR)
        os.makedirs(output_dir_images, exist_ok=True)

        image_paths = {}

        # Thumbnail (400px width)
        thumb = img.copy()
        thumb.thumbnail((400, 400))
        thumb_path_webp = os.path.join(output_dir_images, f"{base_filename}-thumb.webp")
        thumb.save(thumb_path_webp, "webp", quality=80)
        image_paths['thumb_webp'] = f"{IMAGE_ASSETS_DIR}/{os.path.basename(thumb_path_webp)}"
        
        # Full size (no longer resized to preserve quality)
        full_path_webp = os.path.join(output_dir_images, f"{base_filename}-full.webp")
        img.save(full_path_webp, "webp", quality=85)
        image_paths['full_webp'] = f"{IMAGE_ASSETS_DIR}/{os.path.basename(full_path_webp)}"

        # Create JPEG fallbacks
        thumb_path_jpeg = os.path.join(output_dir_images, f"{base_filename}-thumb.jpeg")
        thumb.save(thumb_path_jpeg, "jpeg", quality=80)
        image_paths['thumb_jpeg'] = f"{IMAGE_ASSETS_DIR}/{os.path.basename(thumb_path_jpeg)}"
        
        full_path_jpeg = os.path.join(output_dir_images, f"{base_filename}-full.jpeg")
        img.save(full_path_jpeg, "jpeg", quality=85)
        image_paths['full_jpeg'] = f"{IMAGE_ASSETS_DIR}/{os.path.basename(full_path_jpeg)}"

        return image_paths

    except Exception as e:
        print(f"  - ERROR: Could not process image from {image_source}. Error: {e}")
        raise

def process_author_photo(photo_path, output_dir_base, lang):
    """
    Processes an author's photo, handling both local paths and URLs.
    """
    if not photo_path:
        return None

    output_dir_images = os.path.join(output_dir_base, lang, IMAGE_ASSETS_DIR, "authors")
    os.makedirs(output_dir_images, exist_ok=True)

    image_bytes = None
    base_filename = None

    if photo_path.startswith("http"):
        try:
            response = requests.get(photo_path, timeout=15)
            response.raise_for_status()
            image_bytes = response.content
            url_hash = hashlib.sha1(photo_path.encode()).hexdigest()[:10]
            original_filename = os.path.splitext(os.path.basename(urlparse(photo_path).path))[0]
            base_filename = f"{original_filename}-{url_hash}"
        except requests.exceptions.RequestException as e:
            print(f"  - ERROR: Could not download author image {photo_path}. Error: {e}")
            raise
    elif photo_path.startswith("/public/"):
        local_path = photo_path.lstrip('/')
        if os.path.exists(local_path):
            with open(local_path, "rb") as f:
                image_bytes = f.read()
            base_filename = os.path.splitext(os.path.basename(local_path))[0]
        else:
            print(f"  - ERROR: Could not find local author image {local_path}.")
            raise FileNotFoundError(f"Author image not found at {local_path}")
    else:
        print(f"  - ERROR: Invalid photo path format: {photo_path}. Must be a URL or start with /public/.")
        raise ValueError(f"Invalid author photo path: {photo_path}")

    if not image_bytes or not base_filename:
        raise ValueError("Author image processing failed: image_bytes is empty or base_filename is not set.")

    try:
        img = Image.open(BytesIO(image_bytes))
        img = img.convert("RGB")
        img.thumbnail((200, 200))

        photo_filename_webp = f"{base_filename}.webp"
        photo_filename_jpeg = f"{base_filename}.jpeg"
        
        img.save(os.path.join(output_dir_images, photo_filename_webp), "webp", quality=85)
        img.save(os.path.join(output_dir_images, photo_filename_jpeg), "jpeg", quality=85)

        return {
            'webp': f"../{IMAGE_ASSETS_DIR}/authors/{photo_filename_webp}",
            'jpeg': f"../{IMAGE_ASSETS_DIR}/authors/{photo_filename_jpeg}"
        }
        
    except Exception as e:
        print(f"  - ERROR: Could not process author image {photo_path}. Error: {e}")
        raise

def process_audio(audio_path, output_dir_base, lang):
    """
    Copies a local audio file and saves it, returning its relative path.
    """
    if not audio_path or not os.path.exists(audio_path):
        print(f"  - ERROR: Could not find local audio file {audio_path}.")
        raise FileNotFoundError(f"Audio file not found at {audio_path}")

    try:
        with open(audio_path, "rb") as f:
            audio_bytes = f.read()
            
        content_hash = hashlib.sha1(audio_bytes).hexdigest()[:10]
        original_filename = os.path.basename(audio_path)
        base_name, ext = os.path.splitext(original_filename)
        base_filename = f"{base_name}-{content_hash}{ext}"

        output_dir_audio = os.path.join(output_dir_base, lang, AUDIO_ASSETS_DIR)
        os.makedirs(output_dir_audio, exist_ok=True)

        dest_path = os.path.join(output_dir_audio, base_filename)
        with open(dest_path, "wb") as f:
            f.write(audio_bytes)
        
        relative_path = f"{AUDIO_ASSETS_DIR}/{base_filename}"
        print(f"  - Saved audio to {relative_path}")
        return relative_path

    except Exception as e:
        print(f"  - ERROR: Could not process audio {audio_path}. Error: {e}")
        raise

# --- Translations Dictionary ---
TRANSLATIONS = {
    "rss": {
        "title": {
            "it": "AITalk - Notizie ed Analisi sull'IA",
            "en": "AITalk - AI News and Analysis",
            "es": "AITalk - Noticias y Análisis de IA",
            "fr": "AITalk - Actualités et Analyses en IA",
            "de": "AITalk - KI-Nachrichten und Analysen"
        },
        "description": {
            "it": "Le ultime notizie e approfondimenti sull'intelligenza artificiale, a cura di Dario Ferrero.",
            "en": "The latest news and insights on artificial intelligence, by Dario Ferrero.",
            "es": "Las últimas noticias y análisis sobre inteligencia artificial, por Dario Ferrero.",
            "fr": "Les dernières nouvelles et analyses sur l'intelligence artificielle, par Dario Ferrero.",
            "de": "Die neuesten Nachrichten und Einblicke in die künstliche Intelligenz, von Dario Ferrero."
        }
    },
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
    "newsletter_box": {
        "title": {
            "it": "Ti sta piacendo questo articolo?",
            "en": "Are you enjoying this article?",
            "es": "¿Estás disfrutando de este artículo?",
            "fr": "Vous appréciez cet article ?",
            "de": "Gefällt Ihnen dieser Artikel?"
        },
        "paragraph": {
            "it": "Iscriviti alla newsletter per non perdere i prossimi contenuti. Niente spam, solo approfondimenti di qualità sull'IA.",
            "en": "Subscribe to the newsletter to not miss future content. No spam, only quality insights on AI.",
            "es": "Suscríbete al boletín para no perderte contenido futuro. Sin spam, solo análisis de calidad sobre IA.",
            "fr": "Abonnez-vous à la newsletter pour ne pas manquer les prochains contenus. Pas de spam, juste des analyses de qualité sur l'IA.",
            "de": "Abonnieren Sie den Newsletter, um keine zukünftigen Inhalte zu verpassen. Kein Spam, nur qualitativ hochwertige Einblicke in die KI."
        },
        "button_text": {
            "it": "Iscriviti Gratuitamente",
            "en": "Subscribe for Free",
            "es": "Suscríbete Gratis",
            "fr": "Abonnez-vous Gratuitement",
            "de": "Kostenlos abonnieren"
        }
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
        },
        "editorial_method": {
            "it": "Metodo editoriale",
            "en": "Editorial Method",
            "es": "Método editorial",
            "fr": "Méthode éditoriale",
            "de": "Redaktionelle Methode"
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
        },
        "author_by": {
            "it": "di",
            "en": "by",
            "es": "por",
            "fr": "par",
            "de": "von"
        },
        "listen_to_podcast": {
            "it": "Podcast",
            "en": "Podcast",
            "es": "Podcast",
            "fr": "Podcast",
            "de": "Podcast"
        },
        "watch_video": {
            "it": "Video",
            "en": "Video",
            "es": "Video",
            "fr": "Vidéo",
            "de": "Video"
        },
        "back_to_top_button": {
            "it": "Torna su",
            "en": "Back to top",
            "es": "Volver arriba",
            "fr": "Retour en haut",
            "de": "Nach oben"
        }
    },
    "author_page": {
        "page_title_suffix": {
            "it": "Autore su AITalk",
            "en": "Author at AITalk",
            "es": "Autor en AITalk",
            "fr": "Auteur chez AITalk",
            "de": "Autor bei AITalk"
        },
        "biography": {
            "it": "Biografia",
            "en": "Biography",
            "es": "Biografía",
            "fr": "Biographie",
            "de": "Biografie"
        },
        "latest_articles": {
            "it": "Ultimi Articoli",
            "en": "Latest Articles",
            "es": "Últimos Artículos",
            "fr": "Derniers Articles",
            "de": "Neueste Artikel"
        },
        "no_articles_found": {
            "it": "Nessun articolo trovato per questo autore.",
            "en": "No articles found for this author.",
            "es": "No se encontraron artículos de este autor.",
            "fr": "Aucun article trouvé pour cet auteur.",
            "de": "Keine Artikel für diesen Autor gefunden."
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
            "it": "Verifica Assenza Cookie",
            "en": "Verify Cookie Absence",
            "es": "Verificar Ausencia de Cookies",
            "fr": "Vérifier l'Absence de Cookies",
            "de": "Cookie-Abwesenheit prüfen"
        },
        "link_url": {
            "it": "https://www.cookieserve.com/it/scan-summary/?url=https%3A%2F%2Faitalk.it%2Fit%2F",
            "en": "https://www.cookieserve.com/scan-summary/?url=https%3A%2F%2Faitalk.it%2Fen%2F",
            "es": "https://www.cookieserve.com/es/scan-summary/?url=https%3A%2F%2Faitalk.it%2Fes%2F",
            "fr": "https://www.cookieserve.com/fr/scan-summary/?url=https%3A%2F%2Faitalk.it%2Ffr%2F",
            "de": "https://www.cookieserve.com/de/scan-summary/?url=https%3A%2F%2Faitalk.it%2Fde%2F"
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
            "es": "Este sitio no recopila datos personales de ningún tipo, a excepción del nome y la dirección de correo electrónico proporcionados voluntariamente por los usuarios que se suscriben a nuestro boletín. Nuestro objetivo no es recopilar información sobre usted, sino compartir la pasión por la inteligencia artificial y el mundo de la tecnología.",
            "fr": "Ce site ne collecte aucune donnée personnelle, à l'exception du nom et de l'adresse e-mail fournis volontariamente par les utilisateurs qui s'abonnent à notre newsletter. Notre obiettivo n'est pas de collecter des informations sur vous, mais de partager la passion pour l'intelligence artificielle et le monde de la technologie.",
            "de": "Diese Website sammelt keinerlei personenbezogene Daten, mit Ausnahme des Namens und der E-Mail-Adresse, die von Benutzern, die unseren Newsletter abonnieren, freiwillig angegeben werden. Unser Ziel ist es nicht, Informationen über Sie zu sammeln, sondern die Leidenschaft für künstliche Intelligenz und die Tech-Welt zu teilen."
        },
        "p2": {
            "it": "I dati forniti (nome ed email) vengono utilizzati esclusivamente per inviarti aggiornamenti, articoli e novità tramite la nostra newsletter. Non condivideremo mai queste informazioni con terze parti senza il tuo esplicito consenso.",
            "en": "The data provided (name and email) are used exclusively to send you updates, articles, and news through our newsletter. We will never share this information with third parties without your explicit consent.",
            "es": "Los datos proporcionados (nombre y correo electrónico) se utilizan exclusivamente para enviarle actualizaciones, artículos y noticias a través de nostro boletín. Nunca compartiremos esta información con terceros sin su consentimiento explícito.",
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
    "metodo_page": {
        "title": {
            "it": "Metodo editoriale",
            "en": "Editorial Method",
            "es": "Método editorial",
            "fr": "Méthode éditoriale",
            "de": "Redaktionelle Methode"
        },
        "h1": {
            "it": "Dietro le quinte: come nascono le analisi di AITalk",
            "en": "Behind the scenes: how AITalk analyses are born",
            "es": "Entre bastidores: cómo nacen los análisis de AITalk",
            "fr": "Dans les coulisses : comment naissent les analyses d'AITalk",
            "de": "Hinter den Kulissen: Wie die AITalk-Analysen entstehen"
        },
        "h2_1": {
            "it": "L'idea prima degli strumenti",
            "en": "The idea before the tools",
            "es": "La idea antes que las herramientas",
            "fr": "L'idée avant les outils",
            "de": "Die Idee vor den Werkzeugen"
        },
        "p1": {
            "it": "Ogni analisi pubblicata su questo portale inizia nello stesso modo in cui è sempre iniziato un articolo: con la ricerca di una storia che valga la pena raccontare. Scorro giornali specializzati, blog tecnici, social network, YouTube, archivi di ricerche accademiche. Non cerco l'hype del momento, quello che tutti stanno già commentando. Cerco argomenti di sostanza, innovazioni effettive o prospettiche che si nascondono lontano dai riflettori. A volte sono questioni puramente tecniche che però portano con sé collegamenti etici, sociali, culturali, economici o geopolitici. È in questi interstizi che si annidano le storie più interessanti. Ecco l'angolo narrativo: non solo \"cosa hanno fatto\", ma \"perché l'hanno fatto così\" e \"cosa significa nel contesto più ampio della competizione tecnologica globale\".",
            "en": "Every analysis published on this portal starts the same way an article has always started: with the search for a story worth telling. I scroll through specialized newspapers, technical blogs, social networks, YouTube, archives of academic research. I don't look for the hype of the moment, what everyone is already commenting on. I look for substantive topics, effective or prospective innovations that are hidden away from the spotlight. Sometimes they are purely technical issues that nevertheless bring with them ethical, social, cultural, economic or geopolitical connections. It is in these interstices that the most interesting stories lurk. Here is the narrative angle: not just \"what they did\", but \"why they did it that way\" and \"what it means in the broader context of global technological competition\".",
            "es": "Cada análisis publicado en este portal comienza de la misma manera que siempre ha comenzado un artículo: con la búsqueda de una historia que valga la pena contar. Recorro periódicos especializados, blogs técnicos, redes sociales, YouTube, archivos de investigaciones académicas. No busco el hype del momento, lo que todo el mundo ya está comentando. Busco temas de fondo, innovaciones reales o prospectivas que se esconden lejos de los focos. A veces son cuestiones puramente técnicas que, sin embargo, conllevan conexiones éticas, sociales, culturales, económicas o geopolíticas. Es en estos intersticios donde se esconden las historias más interesantes. He aquí el ángulo narrativo: no solo \"qué hicieron\", sino \"por qué lo hicieron así\" y \"qué significa en el contexto más amplio de la competencia tecnológica global\".",
            "fr": "Chaque analyse publiée sur ce portail commence de la même manière qu'un article a toujours commencé : par la recherche d'une histoire qui mérite d'être racontée. Je parcours les journaux spécialisés, les blogs techniques, les réseaux sociaux, YouTube, les archives de recherche académique. Je ne cherche pas le buzz du moment, ce que tout le monde commente déjà. Je cherche des sujets de fond, des innovations réelles ou prospectives qui se cachent loin des projecteurs. Parfois, il s'agit de questions purement techniques qui portent néanmoins en elles des liens éthiques, sociaux, culturels, économiques ou géopolitiques. C'est dans ces interstices que se nichent les histoires les plus intéressantes. Voici l'angle narratif : non seulement « ce qu'ils ont fait », mais « pourquoi ils l'ont fait ainsi » et « ce que cela signifie dans le contexte plus large de la compétition technologique mondiale ».",
            "de": "Jede auf diesem Portal veröffentlichte Analyse beginnt auf dieselbe Weise, wie ein Artikel schon immer begonnen hat: mit der Suche nach einer Geschichte, die es wert ist, erzählt zu werden. Ich durchforste Fachzeitungen, technische Blogs, soziale Netzwerke, YouTube, Archive akademischer Forschung. Ich suche nicht nach dem Hype des Augenblicks, dem, was alle bereits kommentieren. Ich suche nach substanziellen Themen, effektiven oder perspektivischen Innovationen, die sich abseits des Rampenlichts verbergen. Manchmal sind es rein technische Fragen, die jedoch ethische, soziale, kulturelle, wirtschaftliche oder geopolitische Verbindungen mit sich bringen. In diesen Zwischenräumen nisten die interessantesten Geschichten. Hier ist der erzählerische Blickwinkel: nicht nur \"was sie getan haben\", sondern \"warum sie es so getan haben\" und \"was es im größeren Kontext des globalen technologischen Wettbewerbs bedeutet\"."
        },
        "h2_2": {
            "it": "La ricerca: da Google a Perplexity",
            "en": "Research: from Google to Perplexity",
            "es": "La investigación: de Google a Perplexity",
            "fr": "La recherche : de Google à Perplexity",
            "de": "Die Recherche: von Google bis Perplexity"
        },
        "p2_1": {
            "it": "Una volta identificata l'idea, inizia il lavoro di scavo. La prima fase è quella classica: una ricerca manuale su Google per orientarmi, capire chi ha già scritto cosa, individuare le fonti primarie. Poi passo a Perplexity, uno strumento AI specializzato nella ricerca e nell'aggregazione di fonti che ho trovato particolarmente affidabile. Non si tratta di delegare la ricerca all'intelligenza artificiale, ma di usarla come amplificatore: Perplexity mi permette di esplorare connessioni che richiederebbero ore di lavoro manuale, indicizzando rapidamente paper accademici, comunicati stampa ufficiali, discussioni tecniche su forum specializzati.",
            "en": "Once the idea has been identified, the excavation work begins. The first phase is the classic one: a manual search on Google to orient myself, understand who has already written what, identify primary sources. Then I move on to Perplexity, an AI tool specialized in research and source aggregation that I have found particularly reliable. It's not about delegating research to artificial intelligence, but about using it as an amplifier: Perplexity allows me to explore connections that would require hours of manual work, quickly indexing academic papers, official press releases, technical discussions on specialized forums.",
            "es": "Una vez identificada la idea, comienza el trabajo de excavación. La primera fase es la clásica: una búsqueda manual en Google para orientarme, entender quién ha escrito ya qué, identificar fuentes primarias. Luego paso a Perplexity, una herramienta de IA especializada en la investigación y agregación de fuentes que me ha parecido particularmente fiable. No se trata de delegar la investigación en la inteligencia artificial, sino de usarla como amplificador: Perplexity me permite explorar conexiones que requerirían horas de trabajo manual, indexando rápidamente artículos académicos, comunicados de prensa oficiales, discusiones técnicas en foros especializados.",
            "fr": "Une fois l'idée identifiée, le travail de fouille commence. La première phase est classique : une recherche manuelle sur Google pour m'orienter, comprendre qui a déjà écrit quoi, identifier les sources primaires. Ensuite, je passe à Perplexity, un outil d'IA spécialisé dans la recherche et l'agrégation de sources que j'ai trouvé particulièrement fiable. Il ne s'agit pas de déléguer la recherche à l'intelligence artificielle, mais de l'utiliser comme un amplificateur : Perplexity me permet d'explorer des connexions qui nécessiteraient des heures de travail manuel, en indexant rapidement des articles académiques, des communiqués de presse officiels, des discussions techniques sur des forums spécialisés.",
            "de": "Sobald die Idee identifiziert ist, beginnt die Grabungsarbeit. Die erste Phase ist die klassische: eine manuelle Suche auf Google, um mich zu orientieren, zu verstehen, wer bereits was geschrieben hat, und Primärquellen zu identifizieren. Dann wechsle ich zu Perplexity, einem KI-Tool, das auf Recherche und Aggregation von Quellen spezialisiert ist und das ich als besonders zuverlässig empfunden habe. Es geht nicht darum, die Recherche an die künstliche Intelligenz zu delegieren, sondern sie als Verstärker zu nutzen: Perplexity ermöglicht es mir, Verbindungen zu erkunden, die Stunden manueller Arbeit erfordern würden, indem es akademische Paper, offizielle Pressemitteilungen und technische Diskussionen in Fachforen schnell indiziert."
        },
        "p2_2": {
            "it": "Dopo aver letto le fonti primarie, faccio quello che chiamo un \"brainstorming assistito\" con Perplexity: identifico cinque o sei punti essenziali su cui indagare per costruire un'analisi completa a trecentosessanta gradi. È ancora un lavoro profondamente umano: l'AI suggerisce, io decido cosa vale la pena approfondire e cosa scartare.",
            "en": "After reading the primary sources, I do what I call \"assisted brainstorming\" with Perplexity: I identify five or six essential points to investigate to build a complete three-hundred-and-sixty-degree analysis. It is still deeply human work: the AI suggests, I decide what is worth exploring further and what to discard.",
            "es": "Tras leer las fuentes primarias, hago lo que llamo una \"lluvia de ideas asistida\" con Perplexity: identifico cinco o seis puntos esenciales a investigar para construir un análisis completo de trescientos sesenta grados. Sigue siendo un trabajo profundamente humano: la IA sugiere, yo decido qué vale la pena profundizar y qué descartar.",
            "fr": "Après avoir lu les sources primaires, je fais ce que j'appelle un « brainstorming assisté » avec Perplexity : j'identifie cinq ou six points essentiels à approfondir pour construire une analyse complète à trois cent soixante degrés. C'est encore un travail profondément humain : l'IA suggère, je décide de ce qui mérite d'être approfondi et de ce qu'il faut écarter.",
            "de": "Nach dem Lesen der Primärquellen mache ich das, was ich ein \"unterstütztes Brainstorming\" mit Perplexity nenne: Ich identifiziere fünf oder sechs wesentliche Punkte, die untersucht werden müssen, um eine vollständige 360-Grad-Analyse zu erstellen. Es ist immer noch eine zutiefst menschliche Arbeit: Die KI schlägt vor, ich entscheide, was es wert ist, vertieft zu werden, und was verworfen wird."
        },
        "h2_3": {
            "it": "Lo scheletro dell'analisi",
            "en": "The skeleton of the analysis",
            "es": "El esqueleto del análisis",
            "fr": "Le squelette de l'analyse",
            "de": "Das Skelett der Analyse"
        },
        "p3_1": {
            "it": "A questo punto costruisco uno schema dettagliato di come voglio sviluppare l'articolo. Definisco il tono, cerco un filo rosso narrativo che tenga insieme i diversi piani dell'analisi, ragiono sull'incipit e sul finale, penso ad eventuali metafore culturali che possano alleggerire la lettura senza banalizzarla. Riferimenti pop non mainstream, analogie da nicchie culturali, citazioni di cult movie o videogiochi narrativi: tutto serve a rendere accessibile la complessità senza svilirla.",
            "en": "At this point I build a detailed outline of how I want to develop the article. I define the tone, look for a narrative red thread that holds the different levels of analysis together, think about the opening and the ending, think about possible cultural metaphors that can lighten the reading without trivializing it. Non-mainstream pop references, analogies from cultural niches, quotes from cult movies or narrative video games: everything serves to make complexity accessible without debasing it.",
            "es": "En este punto, construyo un esquema detallado de cómo quiero desarrollar el artículo. Defino el tono, busco un hilo conductor narrativo que mantenga unidos los diferentes niveles del análisis, pienso en el inicio y el final, pienso en posibles metáforas culturales que puedan aligerar la lectura sin banalizarla. Referencias pop no convencionales, analogías de nichos culturales, citas de películas de culto o videojuegos narrativos: todo sirve para hacer accesible la complejidad sin degradarla.",
            "fr": "À ce stade, je construis un schéma détaillé de la manière dont je veux développer l'article. Je définis le ton, je cherche un fil rouge narratif qui lie les différents niveaux de l'analyse, je réfléchis à l'accroche et à la fin, je pense à d'éventuelles métaphores culturelles qui pourraient alléger la lecture sans la banaliser. Références pop non-mainstream, analogies issues de niches culturelles, citations de films cultes ou de jeux vidéo narratifs : tout sert à rendre la complexité accessible sans l'avilir.",
            "de": "An diesem Punkt erstelle ich einen detaillierten Entwurf, wie ich den Artikel entwickeln möchte. Ich definiere den Tonfall, suche nach einem erzählerischen roten Faden, der die verschiedenen Ebenen der Analyse zusammenhält, überlege mir den Anfang und das Ende und denke an mögliche kulturelle Metaphern, die das Lesen auflockern können, ohne es zu banalisieren. Nicht-Mainstream-Pop-Referenzen, Analogien aus kulturellen Nischen, Zitate aus Kultfilmen oder erzählerischen Videospielen: Alles dient dazu, Komplexität zugänglich zu machen, ohne sie herabzuwürdigen."
        },
        "p3_2": {
            "it": "Poi riempio questo scheletro con i contenuti estratti dalle varie fonti, verificando ogni dato, ogni citazione, ogni collegamento logico. Questa prima bozza, che generalmente occupa circa tre cartelle Word, è già un testo strutturato e referenziato, non una raccolta casuale di appunti. È il materiale grezzo ma organizzato che poi affinerò.",
            "en": "Then I fill this skeleton with the content extracted from various sources, verifying every piece of data, every quote, every logical connection. This first draft, which generally takes up about three Word pages, is already a structured and referenced text, not a random collection of notes. It is the raw but organized material that I will then refine.",
            "es": "Luego relleno este esqueleto con el contenido extraído de las diversas fuentes, verificando cada dato, cada cita, cada conexión lógica. Este primer borrador, que generalmente ocupa unas tres páginas de Word, ya es un texto estructurado y referenciado, no una colección aleatoria de notas. Es el material en bruto pero organizado que luego refinaré.",
            "fr": "Ensuite, je remplis ce squelette avec le contenu extrait des diverses sources, en vérifiant chaque donnée, chaque citation, chaque lien logique. Ce premier brouillon, qui occupe généralement environ trois pages Word, est déjà un texte structuré et référencé, pas une collection aléatoire de notes. C'est le matériau brut mais organisé que j'affinerai ensuite.",
            "de": "Dann fülle ich dieses Skelett mit den aus den verschiedenen Quellen extrahierten Inhalten und überprüfe jedes Datum, jedes Zitat, jede logische Verbindung. Dieser erste Entwurf, der in der Regel etwa drei Word-Seiten umfasst, ist bereits ein strukturierter und mit Quellen versehener Text, keine zufällige Sammlung von Notizen. Er ist das rohe, aber organisierte Material, das ich dann verfeinern werde."
        },
        "h2_4": {
            "it": "Claude entra in scena",
            "en": "Claude enters the scene",
            "es": "Claude entra en escena",
            "fr": "Claude entre en scène",
            "de": "Claude betritt die Bühne"
        },
        "p4_1": {
            "it": "Solo a questo punto entra in gioco Claude, il modello linguistico di Anthropic che uso per la stesura finale. Gli fornisco la mia bozza insieme a un prompt che ho affinato nel tempo, dove definisco identità e stile del portale, il tono di voce, l'approccio critico che voglio mantenere, il processo di lavoro e una checklist finale. Claude mi restituisce una proposta di sviluppo che affino una o due volte, generalmente arrivando rapidamente a qualcosa di molto vicino alla mia visione grazie al lavoro pregresso sul prompt.",
            "en": "Only at this point does Claude come into play, the language model from Anthropic that I use for the final drafting. I provide him with my draft together with a prompt that I have refined over time, where I define the identity and style of the portal, the tone of voice, the critical approach I want to maintain, the work process and a final checklist. Claude gives me back a development proposal that I refine once or twice, generally quickly arriving at something very close to my vision thanks to the previous work on the prompt.",
            "es": "Solo en este punto entra en juego Claude, el modelo lingüístico de Anthropic que utilizo para la redacción final. Le proporciono mi borrador junto con un prompt que he ido perfeccionando con el tiempo, donde defino la identidad y el estilo del portal, el tono de voz, el enfoque crítico que quiero mantener, el proceso de trabajo y una lista de verificación final. Claude me devuelve una propuesta de desarrollo que afino una o dos veces, llegando generalmente rápido a algo muy cercano a mi visión gracias al trabajo previo sobre el prompt.",
            "fr": "Ce n'est qu'à ce moment-là qu'intervient Claude, le modèle linguistique d'Anthropic que j'utilise pour la rédaction finale. Je lui fournis mon brouillon accompagné d'un prompt que j'ai affiné au fil du temps, où je définis l'identité et le style du portail, le ton de la voix, l'approche critique que je veux maintenir, le processus de travail et une checklist finale. Claude me renvoie une proposition de développement que j'affine une ou deux fois, arrivant généralement rapidement à quelque chose de très proche de ma vision grâce au travail préalable sur le prompt.",
            "de": "Erst an diesem Punkt kommt Claude ins Spiel, das Sprachmodell von Anthropic, das ich für die endgültige Fassung verwende. Ich stelle ihm meinen Entwurf zusammen mit einem Prompt zur Verfügung, den ich im Laufe der Zeit verfeinert habe, in dem ich die Identität und den Stil des Portals, den Tonfall, den kritischen Ansatz, den ich beibehalten möchte, den Arbeitsprozess und eine abschließende Checkliste definiere. Claude liefert mir einen Entwicklungsvorschlag, den ich ein- oder zweimal verfeinere, wobei ich dank der Vorarbeit am Prompt in der Regel schnell zu etwas komme, das meiner Vision sehr nahe kommt."
        },
        "p4_2": {
            "it": "È importante chiarire cosa fa Claude in questo processo: non scrive l'articolo al posto mio, lo riscrive seguendo parametri precisi che io ho definito. Trasforma la mia bozza tecnica in una narrazione più fluida, mantiene coerenza stilistica, suggerisce connessioni che potrebbero essere sfuggite. Ma il controllo resta interamente umano. Claude è uno strumento di editing avanzato, non un coautore.",
            "en": "It is important to clarify what Claude does in this process: he doesn't write the article in my place, he rewrites it following precise parameters that I have defined. He transforms my technical draft into a more fluid narrative, maintains stylistic consistency, suggests connections that might have been missed. But control remains entirely human. Claude is an advanced editing tool, not a co-author.",
            "es": "Es importante aclarar qué hace Claude en este proceso: no escribe el artículo por mí, lo redacta siguiendo parámetros precisos que yo he definido. Transforma mi borrador técnico en una narración más fluida, mantiene la coherencia estilística, sugiere conexiones que podrían haber pasado desapercibidas. Pero el control sigue siendo enteramente humano. Claude es una herramienta de edición avanzada, no un coautor.",
            "fr": "Il est important de préciser ce que fait Claude dans ce processus : il n'écrit pas l'article à ma place, il le réécrit suivant des paramètres précis que j'ai définis. Il transforme mon brouillon technique en une narration plus fluide, maintient la cohérence stylistique, suggère des connexions qui auraient pu m'échapper. Mais le contrôle reste entièrement humain. Claude est un outil d'édition avancé, pas un co-auteur.",
            "de": "Es wichtig zu klären, was Claude in diesem Prozess tut: Er schreibt den Artikel nicht an meiner Stelle, er schreibt ihn nach präzisen Parametern um, die ich definiert habe. Er verwandelt meinen technischen Entwurf in eine flüssigere Erzählung, wahrt die stilistische Konsistenz und schlägt Verbindungen vor, die möglicherweise übersehen wurden. Aber die Kontrolle bleibt vollständig in menschlicher Hand. Claude ist ein fortgeschrittenes Bearbeitungswerkzeug, kein Mitautor."
        },
        "h2_5": {
            "it": "La revisione è tutto",
            "en": "Revision is everything",
            "es": "La revisión lo es todo",
            "fr": "La révision est tout",
            "de": "Überprüfung ist alles"
        },
        "p5_1": {
            "it": "Qui arriva la parte più impegnativa e che richiede la massima attenzione critica. I modelli linguistici sono convincenti nelle loro asserzioni, ed è proprio questa sicurezza apparente a rappresentare una trappola psicologica: bisogna verificare tutto. Inizio una revisione totale del testo, correggendo le parti che non mi convincono, verificando ogni singola citazione e fonte. Claude, sulla base del mio testo e delle fonti che gli ho fornito, a volte integra autonomamente la ricerca o inserisce collegamenti aggiuntivi. Se queste integrazioni mi sembrano utili per arricchire l'analisi, le tengo solo dopo opportune verifiche. Se non aggiungono valore o se non riesco a confermarle attraverso fonti primarie affidabili, le taglio senza esitazione.",
            "en": "Here comes the most demanding part, requiring maximum critical attention. Language models are convincing in their assertions, and it is precisely this apparent certainty that represents a psychological trap: everything must be verified. I begin a total revision of the text, correcting the parts that don't convince me, verifying every single quote and source. Claude, based on my text and the sources I provided him, sometimes independently integrates research or inserts additional links. If these integrations seem useful to me to enrich the analysis, I keep them only after appropriate verification. If they don't add value or if I can't confirm them through reliable primary sources, I cut them without hesitation.",
            "es": "Aquí llega la parte más exigente, que requiere la máxima atención crítica. Los modelos lingüísticos son convincentes en sus afirmaciones, y es precisamente esta seguridad aparente la que representa una trampa psicológica: hay que verificarlo todo. Comienzo una revisión total del texto, corrigiendo las partes que no me convencen, verificando cada cita y fuente. Claude, basándose en mi texto y en las fuentes que le he proporcionado, a veces integra la investigación de forma autónoma o inserta enlaces adicionales. Si estas integraciones me parecen útiles para enriquecer el análisis, las mantengo solo después de las verificaciones oportunas. Si no aportan valor o si no puedo confirmarlas a través de fuentes primarias fiables, las elimino sin vacilación.",
            "fr": "C'est ici que commence la partie la plus exigeante, celle qui demande la plus grande attention critique. Les modèles linguistiques sont convaincants dans leurs affirmations, et c'est précisément cette assurance apparente qui représente un piège psychologique : il faut tout vérifier. Je commence une révision totale du texte, en corrigeant les parties qui ne me convainquent pas, en vérifiant chaque citation et source. Claude, sur la base de mon texte et des sources que je lui ai fournies, intègre parfois de lui-même des recherches ou insère des liens supplémentaires. Si ces intégrations me semblent utiles pour enrichir l'analyse, je ne les garde qu'après les vérifications d'usage. Si elles n'apportent pas de valeur ajoutée ou si je ne parviens pas à les confirmer par des sources primaires fiables, je les coupe sans hésitation.",
            "de": "Hier kommt der anspruchsvollste Teil, der höchste kritische Aufmerksamkeit erfordert. Sprachmodelle sind in ihren Behauptungen überzeugend, und genau diese scheinbare Sicherheit stellt eine psychologische Falle dar: Alles muss überprüft werden. Ich beginne eine vollständige Überarbeitung des Textes, korrigiere die Teile, die mich nicht überzeugen, und überprüfe jedes einzelne Zitat und jede Quelle. Claude integriert auf der Grundlage meines Textes und der Quellen, die ich ihm zur Verfügung gestellt habe, manchmal selbstständig Recherchen oder fügt zusätzliche Links ein. Wenn mir diese Ergänzungen nützlich erscheinen, um die Analyse zu bereichern, behalte ich sie nur nach entsprechenden Überprüfungen bei. Wenn sie keinen Mehrwert bieten oder ich sie nicht durch zuverlässige Primärquellen bestätigen kann, schneide ich sie ohne Zögern heraus."
        },
        "p5_2": {
            "it": "Ogni affermazione deve avere un link verificato. Non accetto riferimenti generici o citazioni non tracciabili. Questo controllo maniacale, secondo me, è ciò che distingue un'analisi di qualità da un contenuto generato in massa. È un lavoro lungo, a tratti noioso, assolutamente fondamentale. Come nel montaggio cinematografico, il regista può avere ottimi strumenti di editing, ma la decisione su quale inquadratura tenere e quale scartare resta sua e solo sua.",
            "en": "Every statement must have a verified link. I do not accept generic references or untraceable quotes. This obsessive control, in my opinion, is what distinguishes a quality analysis from mass-generated content. It is a long, sometimes tedious, absolutely fundamental job. As in film editing, the director may have excellent editing tools, but the decision on which shot to keep and which to discard remains theirs and theirs alone.",
            "es": "Cada afirmación debe tener un enlace verificado. No acepto referencias genéricas ni citas no rastreables. Este control obsesivo es, en mi opinión, lo que distingue un análisis de calidad de un contenido generado en masa. Es un trabajo largo, a veces tedioso, absolutamente fundamental. Como en el montaje cinematográfico, el director puede tener excelentes herramientas de edición, pero la decisión sobre qué plano mantener y cuál descartar sigue siendo suya y solo suya.",
            "fr": "Chaque affirmation doit avoir un lien vérifié. Je n'accepte pas de références génériques ou de citations non traçables. Ce contrôle obsessionnel est, selon moi, ce qui distingue une analyse de qualité d'un contenu généré en masse. C'est un travail long, parfois fastidieux, absolument fondamental. Comme pour le montage cinématographique, le réalisateur peut disposer d'excellent outils de montage, mais la décision de garder ou de rejeter un plan lui appartient à lui seul.",
            "de": "Jede Aussage muss einen verifizierten Link haben. Ich akzeptiere keine pauschalen Verweise oder nicht nachverfolgbaren Zitate. Diese obsessive Kontrolle ist meiner Meinung nach das, was eine Qualitätsanalyse von massengenerierten Inhalten unterscheidet. Es ist eine lange, manchmal mühsame, absolut grundlegende Arbeit. Wie beim Filmschnitt mag der Regisseur über hervorragende Bearbeitungswerkzeuge verfügen, aber die Entscheidung, welche Einstellung er behält und welche er verwirft, bleibt seine und nur seine."
        },
        "h2_6": {
            "it": "Il packaging multimediale",
            "en": "Multimedia packaging",
            "es": "El packaging multimedia",
            "fr": "Le packaging multimédia",
            "de": "Das multimediale Packaging"
        },
        "p6_1": {
            "it": "Terminata la revisione del testo, cerco immagini che possano integrare l'analisi, preferibilmente da paper ufficiali o fonti verificate, linkando sempre la provenienza. Poi creo l'immagine di copertina: penso a un'immagine che richiami immediatamente il concetto fondamentale dell'articolo, la trasformo in un prompt e la genero con strumenti AI come Leonardo AI o Whisk. Formatto quindi tutto il materiale, testo e immagini, in formato Markdown adatto al backend del portale.",
            "en": "Once the revision of the text is finished, I look for images that can complement the analysis, preferably from official papers or verified sources, always linking the source. Then I create the cover image: I think of an image that immediately recalls the fundamental concept of the article, I transform it into a prompt and generate it with AI tools like Leonardo AI or Whisk. I then format all the material, text and images, in Markdown format suitable for the portal's backend.",
            "es": "Terminada la revisión del texto, busco imágenes que puedan complementar el análisis, preferiblemente de artículos oficiales o fuentes verificadas, enlazando siempre la procedencia. Luego creo la imagen de portada: pienso en una imagen que evoque inmediatamente el concepto fundamental del artículo, la transformo en un prompt y la genero con herramientas de IA como Leonardo AI o Whisk. A continuación, doy formato a todo el material, texto e imágenes, en formato Markdown apto para el backend del portal.",
            "fr": "Une fois la révision du texte terminée, je cherche des images qui peuvent compléter l'analyse, de préférence issues d'articles officiels ou de sources vérifiées, en indiquant toujours la provenance. Ensuite, je crée l'image de couverture : je pense à une image qui évoque immédiatement le concept fondamental de l'article, la transforme en prompt et je la génère avec des outils d'IA comme Leonardo AI ou Whisk. Je formate ensuite tout le matériel, texte et images, au format Markdown adapté au backend du portail.",
            "de": "Nach Abschluss der Textüberarbeitung suche ich nach Bildern, die die Analyse ergänzen können, vorzugsweise aus offiziellen Papern oder verifizierten Quellen, wobei ich immer die Herkunft verlinke. Dann erstelle ich das Titelbild: Ich denke an ein Bild, das sofort das Grundkonzept des Artikels hervorruft, wandle es in einen Prompt um und generiere es mit KI-Werkzeugen wie Leonardo AI oder Whisk. Dann formatiere ich das gesamte Material, Text und Bilder, im Markdown-Format, das für das Backend des Portals geeignet ist."
        },
        "p6_2": {
            "it": "A questo punto genero i contenuti collaterali con NotebookLM: la sintesi video, il podcast audio, l'infografica. Uso prompt mirati per mantenere coerenza stilistica. Infine, siccome il portale è pensato multilingua, genero le traduzioni in inglese, spagnolo, francese e tedesco con Jules, uno strumento che tecnicamente non è nato per questo scopo ma che ho trovato particolarmente efficace e comodo essendo collegato al mio progetto AITalk su GitHub.",
            "en": "At this point I generate collateral content with NotebookLM: the video summary, the audio podcast, the infographic. I use targeted prompts to maintain stylistic consistency. Finally, since the portal is designed to be multilingual, I generate translations in English, Spanish, French and German with Jules, a tool that technically was not born for this purpose but that I have found particularly effective and convenient being connected to my AITalk project on GitHub.",
            "es": "En este punto, genero los contenidos colaterales con NotebookLM: el resumen de vídeo, el podcast de audio, la infografía. Utilizo prompts específicos para mantener la coherencia estilística. Por último, como el portal está pensado para ser multilingüe, genero las traducciones al inglés, español, francés y alemán con Jules, una herramienta que técnicamente no nació para este fin pero que me ha resultado particularmente eficaz y cómoda al estar conectada a mi proyecto AITalk en GitHub.",
            "fr": "À ce stade, je génère les contenus collatéraux avec NotebookLM : le résumé vidéo, le podcast audio, l'infographie. J'utilise des prompts ciblés pour maintenir la cohérence stylistique. Enfin, comme le portail est conçu pour être multilingue, je génère les traductions en anglais, espagnol, français et allemand avec Jules, un outil qui n'est techniquement pas né pour cela mais que j'ai trouvé particulièrement efficace et pratique car il est connecté à mon projet d'AITalk sur GitHub.",
            "de": "An diesem Punkt generiere ich die Begleitinhalte mit NotebookLM: die Videozusammenfassung, den Audio-Podcast, die Infografik. Ich verwende gezielte Prompts, um die stilistische Konsistenz zu wahren. Schließlich, da das Portal mehrsprachig konzipiert ist, generiere ich die Übersetzungen ins Englische, Spanische, Französische und Deutsche mit Jules, einem Werkzeug, das technisch gesehen nicht für diesen Zweck geboren wurde, das ich aber als besonders effektiv und bequem empfunden habe, da es mit meinem AITalk-Projekt auf GitHub verbunden ist."
        },
        "p7": {
            "it": "Il risultato finale lo potete giudicare voi stessi, articolo per articolo, verificando fonti e collegamenti, valutando la solidità delle argomentazioni. La trasparenza su questo processo non è solo un principio etico, è un invito al controllo incrociato. In un'epoca in cui le content farm basate su AI producono migliaia di articoli al giorno senza supervisione umana, rendere visibile il metodo di lavoro diventa parte integrante della credibilità. L'intelligenza artificiale è uno strumento formidabile, ma solo quando resta esattamente questo: uno strumento nelle mani di chi ha ancora qualcosa da dire.",
            "en": "The final result you can judge for yourself, article by article, verifying sources and connections, evaluating the solidity of the arguments. Transparency about this process is not just an ethical principle, it is an invitation to cross-checking. In an era where AI-based content farms produce thousands of articles a day without human supervision, making the work method visible becomes an integral part of credibility. Artificial intelligence is a formidable tool, but only when it remains exactly that: a tool in the hands of those who still have something to say.",
            "es": "El resultado final lo podéis juzgar vosotros mismos, artículo por artículo, verificando fuentes y conexiones, evaluando la solidez de los argumentos. La transparencia sobre este proceso no es solo un principio ético, es una invitación al control cruzado. En una época en la que las granjas de contenidos basadas en IA producen miles de artículos al día sin supervisión humana, hacer visible el método de trabajo se convierte en parte integrante de la credibilidad. La inteligencia artificial es una herramienta formidable, pero solo cuando sigue siendo exactamente eso: una herramienta en manos de quien todavía tiene algo que decir.",
            "fr": "Le résultat final, vous pouvez en juger par vous-mêmes, article par article, en vérifiant les sources et les liens, en évaluant la solidité des arguments. La transparence sur ce processus n'est pas seulement un principe éthique, c'est une invitation au contrôle croisé. À une époque où les fermes de contenus basées sur l'IA produisent des milliers d'articles par jour sans supervision humaine, rendre visible la méthode de travail fait partie intégrante de la crédibilité. L'intelligence artificielle est un outil formidable, mais seulement lorsqu'elle reste exactement cela : un outil entre les mains de ceux qui ont encore quelque chose à dire.",
            "de": "Das Endergebnis können Sie selbst beurteilen, Artikel für Artikel, indem Sie Quellen und Verbindungen prüfen und die Solidität der Argumente bewerten. Transparenz über diesen Prozess ist nicht nur ein ethisches Prinzip, sondern eine Aufforderung zur Gegenprobe. In einer Zeit, in der KI-basierte Content-Farmen täglich Tausende von Artikeln ohne menschliche Aufsicht produzieren, wird das Sichtbarmachen der Arbeitsmethode zu einem integralen Bestandteil der Glaubwürdigkeit. Künstliche Intelligenz ist ein formidables Werkzeug, aber nur, wenn sie genau das bleibt: ein Werkzeug in den Händen derer, die noch etwas zu sagen haben."
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
    },
    "index_page": {
        "articles_heading": {
            "it": "Ultimi Articoli dal mondo dell'Intelligenza Artificiale",
            "en": "Latest Articles from the world of Artificial Intelligence",
            "es": "Últimos Artículos del mundo de la Inteligencia Artificial",
            "fr": "Derniers Articles du monde de l'Intelligence Artificielle",
            "de": "Neueste Artikel aus der Welt der Künstlichen Intelligenz"
        }
    }
}

LANGUAGES = ["it", "en", "es", "fr", "de"]
LANG_CONFIG = {
    "it": {"name": "Italiano", "flag": "it.svg", "abbr": "IT"},
    "en": {"name": "English", "flag": "gb.svg", "abbr": "EN"},
    "es": {"name": "Español", "flag": "es.svg", "abbr": "ES"},
    "fr": {"name": "Français", "flag": "fr.svg", "abbr": "FR"},
    "de": {"name": "Deutsch", "flag": "de.svg", "abbr": "DE"},
}

def generate_language_dropdown_html(current_lang, depth=1):
    """
    Generates the complete HTML for the language selector dropdown.
    """
    asset_prefix = "../" * (depth - 1)
    link_prefix = "../" * depth

    current_lang_info = LANG_CONFIG[current_lang]

    toggle_html = f"""<button class="language-dropdown-toggle">
                        <img src="{asset_prefix}flags/{current_lang_info['flag']}" alt="{current_lang_info['name']}" class="language-flag">
                        <span>{current_lang_info['abbr']}</span>
                        <svg class="dropdown-arrow" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
                    </button>"""

    menu_items_html = ""
    for lang_code, lang_info in LANG_CONFIG.items():
        link = f"{link_prefix}{lang_code}/index.html"
        menu_items_html += f"""
                        <a href="{link}" title="{lang_info['name']}">
                            <img src="{asset_prefix}flags/{lang_info['flag']}" alt="{lang_info['name']}" class="language-flag">
                            <span>{lang_info['name']}</span>
                        </a>"""

    dropdown_html = f"""<div class="language-dropdown">
                    {toggle_html}
                    <div class="language-dropdown-menu">{menu_items_html}
                    </div>
                </div>"""
    return dropdown_html

def get_base_template_data(depth):
    """
    Generates a dictionary of common, relative-path-based data for the base template.
    """
    prefix = "../" * (depth - 1)
    data = {
        "{{css_path}}": f"{prefix}style.css",
        "{{favicon_ico_path}}": f"{prefix}favicon.ico",
        "{{favicon_png_path}}": f"{prefix}favicon.png",
        "{{logo_path_webp}}": f"{prefix}logo_vn_ia.webp",
        "{{logo_path_png}}": f"{prefix}logo_vn_ia.png",
        "{{placeholder_image_path}}": f"{prefix}logo_vn_ia.png",
        "{{newsletter_link}}": f"{prefix}newsletter.html",
        "{{cookie_link}}": f"{prefix}cookie.html",
        "{{privacy_link}}": f"{prefix}privacy.html",
        "{{metodo_link}}": f"{prefix}metodo-editoriale.html",
        "{{home_link}}": f"{prefix}index.html" if prefix else "index.html"
    }
    return data

def get_local_articles_db():
    """
    Scans the local 'articoli' directory and builds a database of articles,
    matching markdown files with their language-specific audio files.
    """
    print("Scanning local 'articoli' directory...")
    articles_db = {}
    if not os.path.exists(ARTICLES_DIR):
        print(f"  - WARN: '{ARTICLES_DIR}' directory not found.")
        return articles_db

    # First pass: group all md and mp3 files by their parent directory.
    file_groups = {}
    for root, _, files in os.walk(ARTICLES_DIR):
        article_dir = os.path.basename(root)
        if root == ARTICLES_DIR:
            continue # Skip the root 'articoli' folder itself

        if article_dir not in file_groups:
            file_groups[article_dir] = {'md': [], 'mp3': []}
        
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.endswith('.md'):
                file_groups[article_dir]['md'].append({'path': file_path, 'name': filename})
            elif filename.endswith('.mp3'):
                file_groups[article_dir]['mp3'].append({'path': file_path, 'name': filename})

    # Second pass: build the final DB, associating md files with their mp3s.
    for article_dir, files in file_groups.items():
        mp3_lookup = {os.path.splitext(f['name'])[0]: f['path'] for f in files['mp3']}

        for md_file in files['md']:
            md_basename = os.path.splitext(md_file['name'])[0]
            
            lang = 'it' # Default language
            if md_basename.endswith('_en'): lang = 'en'
            elif md_basename.endswith('_es'): lang = 'es'
            elif md_basename.endswith('_fr'): lang = 'fr'
            elif md_basename.endswith('_de'): lang = 'de'
            
            md_file['audio_path'] = mp3_lookup.get(md_basename)
            md_file['parent_dir'] = article_dir
            
            if article_dir not in articles_db:
                articles_db[article_dir] = {}
            if lang not in articles_db[article_dir]:
                articles_db[article_dir][lang] = []
            
            articles_db[article_dir][lang].append(md_file)
            
    return articles_db

def get_files_for_lang(articles_db, lang='it'):
    """
    Gets all markdown files for a specific language from the structured DB.
    """
    files_for_lang = []
    for article_dir, languages in articles_db.items():
        if lang in languages:
            for file_info in languages[lang]:
                files_for_lang.append(file_info)

    print(f"Found {len(files_for_lang)} markdown files to process for '{lang}'.")
    return files_for_lang


def load_authors(lang='it'):
    """
    Loads author data from the content/authors directory for a specific language.
    """
    print(f"\nLoading author data for language: '{lang}'...")
    authors_db = {}
    authors_dir = "content/authors"
    if not os.path.exists(authors_dir):
        print("  - No authors directory found. Skipping.")
        return authors_db

    all_author_files = [f for f in os.listdir(authors_dir) if f.endswith(".md")]
    
    author_slugs = {}
    for filename in all_author_files:
        slug = re.sub(r'(_[a-z]{2})?\.md$', '', filename)
        if slug not in author_slugs:
            author_slugs[slug] = []
        author_slugs[slug].append(filename)

    for slug, files in author_slugs.items():
        target_filename = None
        base_file = f"{slug}.md"
        lang_file = f"{slug}_{lang}.md"

        if lang == 'it':
            if base_file in files:
                target_filename = base_file
        else:
            if lang_file in files:
                target_filename = lang_file
            elif base_file in files:
                target_filename = base_file
        
        if not target_filename:
            print(f"  - WARN: No suitable file found for author slug '{slug}' and lang '{lang}'.")
            continue

        filepath = os.path.join(authors_dir, target_filename)
        try:
            author_post = frontmatter.load(filepath)
            
            authors_db[slug] = {
                "slug": slug,
                "name": author_post.metadata.get("name"),
                "photo": author_post.metadata.get("photo"),
                "links": author_post.metadata.get("links", {}),
                "bio": markdown2.markdown(author_post.content)
            }
            print(f"  - Loaded author: {author_post.metadata.get('name')} (from {target_filename})")
        except Exception as e:
            print(f"  - ERROR: Could not process author file {target_filename}. Error: {e}")
            raise
    
    return authors_db

def main():
    """
    Main function to build the static site.
    """
    parser = argparse.ArgumentParser(description="Build the static site for a specific language.")
    parser.add_argument('--lang', default=None, help='Language to build (e.g., en, es)')
    parser.add_argument('--master-files', action='store_true', help='Generate only the master files (sitemap.xml, robots.txt).')
    args = parser.parse_args()

    if args.master_files:
        generate_sitemap_xml()
        generate_robots_txt()
        create_root_redirect()
        return

    lang = args.lang
    if not lang:
        print("Error: --lang is required unless generating master files with --master-files.")
        return
    output_dir = os.path.join(BASE_OUTPUT_DIR, lang)

    print(f"Starting build process for language: '{lang}'...")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    image_dir = os.path.join(output_dir, IMAGE_ASSETS_DIR)
    os.makedirs(image_dir, exist_ok=True)

    authors_data = load_authors(lang)
    print(f"Successfully loaded {len(authors_data)} authors.")

    articles_db = get_local_articles_db()
    md_files = get_files_for_lang(articles_db, lang)

    if not md_files:
        print(f"No markdown files found for language '{lang}'. Exiting.")
        return

    processed_articles = []
    s1 = sorted(md_files, key=lambda x: x['name'].lower(), reverse=True)
    sorted_md_files = sorted(s1, key=lambda x: x['parent_dir'], reverse=True)

    for md_file in sorted_md_files:
        article_data = process_article(md_file, BASE_OUTPUT_DIR, lang)
        if article_data:
            processed_articles.append(article_data)

    generate_article_pages(authors_data, processed_articles, output_dir, lang)
    generate_author_pages(authors_data, processed_articles, output_dir, lang)
    generate_index_page(processed_articles, output_dir, lang)
    generate_rss_feed(processed_articles, output_dir, lang)
    generate_local_pages(output_dir, lang)
    generate_404_page(output_dir, lang)
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

def process_article(md_file_info, output_dir_base, lang):
    """
    Reads a local markdown file, processes it, optimizes images, and returns a dict.
    """
    print(f"Processing file: {md_file_info['name']} in {md_file_info['parent_dir']}...")

    try:
        with open(md_file_info['path'], 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        print(f"  - ERROR: Could not read markdown file {md_file_info['path']}. Error: {e}")
        raise

    try:
        post = frontmatter.loads(md_content)
        html_content = markdown2.markdown(post.content, extras=["tables", "fenced-code-blocks", "spoiler"])
        soup = BeautifulSoup(html_content, 'html.parser')

        title = soup.h1.get_text() if soup.h1 else "Titolo non disponibile"
        if soup.h1:
            soup.h1.decompose()

        summary = ""
        all_paragraphs = soup.find_all('p')
        for p in all_paragraphs:
            if p.get_text(strip=True) and not p.find('img'):
                summary = p.get_text()
                break

        for img in soup.find_all('img'):
            original_src = img.get('src')
            if not original_src:
                continue

            processed_paths = process_and_save_image(original_src, output_dir_base, lang, article_dir=md_file_info['parent_dir'])

            if processed_paths:
                picture_tag = soup.new_tag("picture")
                source_webp = soup.new_tag("source", attrs={"srcset": processed_paths['full_webp'], "type": "image/webp"})
                source_jpeg = soup.new_tag("source", attrs={"srcset": processed_paths['full_jpeg'], "type": "image/jpeg"})
                fallback_img = soup.new_tag("img", attrs={"src": processed_paths['full_jpeg'], "alt": img.get('alt', 'Article image'), "loading": "lazy"})
                picture_tag.append(source_webp)
                picture_tag.append(source_jpeg)
                picture_tag.append(fallback_img)
                img.replace_with(picture_tag)

        temp_soup = BeautifulSoup(markdown2.markdown(post.content), 'html.parser')
        first_img_tag = temp_soup.find('img')
        main_image_paths = None
        if first_img_tag and first_img_tag.get('src'):
            main_image_paths = process_and_save_image(first_img_tag['src'], output_dir_base, lang, article_dir=md_file_info['parent_dir'])

        audio_path = None
        if md_file_info.get('audio_path'):
            audio_path = process_audio(md_file_info['audio_path'], output_dir_base, lang)

        # Inject newsletter box
        headings = soup.find_all('h2')
        insertion_point = None

        if len(headings) > 1:
            # Prefer to insert after a middle chapter heading
            insertion_point = headings[len(headings) // 2]
        else:
            # Fallback to inserting in the middle of the article's paragraphs for longer articles
            paragraphs = soup.find_all('p')
            if len(paragraphs) > 5:
                insertion_point = paragraphs[len(paragraphs) // 2]

        if insertion_point:
            box_title = TRANSLATIONS["newsletter_box"]["title"].get(lang, TRANSLATIONS["newsletter_box"]["title"]["it"])
            box_paragraph = TRANSLATIONS["newsletter_box"]["paragraph"].get(lang, TRANSLATIONS["newsletter_box"]["paragraph"]["it"])
            box_button = TRANSLATIONS["newsletter_box"]["button_text"].get(lang, TRANSLATIONS["newsletter_box"]["button_text"]["it"])
            
            newsletter_box_html = f"""
            <div class="newsletter-box">
                <h3>{box_title}</h3>
                <p>{box_paragraph}</p>
                <a href="newsletter.html" class="subscribe-button">{box_button}</a>
            </div>
            """
            insertion_point.insert_before(BeautifulSoup(newsletter_box_html, 'html.parser'))

        final_html_content = str(soup)
        slug = os.path.splitext(md_file_info['name'])[0].strip().replace('_', '-')
        
        return {
            "title": title,
            "summary": summary,
            "image_paths": main_image_paths,
            "html_content": final_html_content,
            "slug": slug,
            "path": f"{slug}.html",
            "tags": post.metadata.get('tags', []),
            "date": post.metadata.get('date', None),
            "author": post.metadata.get('author', None),
            "audio_path": audio_path,
            "youtube_url": post.metadata.get('youtube_url', None)
        }

    except Exception as e:
        print(f"  - ERROR: Error parsing markdown for {md_file_info['name']}: {e}")
        raise

def generate_article_pages(authors_data, articles, output_dir, lang='it'):
    """
    Generates an HTML page for each article.
    """
    print("\nGenerating article pages...")
    with open("templates/base.html", "r", encoding='utf-8') as f:
        base_template = f.read()

    author_name_to_slug = {v['name']: k for k, v in authors_data.items()}

    for article in articles:
        print(f"  - {article['path']}")

        back_button_text = TRANSLATIONS["article_page"]["back_button"].get(lang, TRANSLATIONS["article_page"]["back_button"]["it"])
        back_to_top_button_text = TRANSLATIONS["article_page"]["back_to_top_button"].get(lang, TRANSLATIONS["article_page"]["back_to_top_button"]["it"])

        tags_html = ""
        if article.get('tags'):
            tags_html = '<div class="article-card-tags" style="margin-bottom: 20px;">'
            for tag in article['tags']:
                tags_html += f'<a href="index.html#{tag}" class="tag">{tag}</a>'
            tags_html += '</div>'

        author_html = ""
        author_name = article.get('author')
        if author_name:
            author_prefix = TRANSLATIONS["article_page"]["author_by"].get(lang, TRANSLATIONS["article_page"]["author_by"]["it"])
            author_slug = author_name_to_slug.get(author_name)
            if author_slug:
                author_html = f'<div class="post-author">{author_prefix} <a href="authors/{author_slug}.html">{author_name}</a></div>'
            else:
                author_html = f'<div class="post-author">{author_prefix} {author_name}</div>'

        media_container_html = ""
        podcast_button_html = ""
        if article.get("audio_path"):
            podcast_button_text = TRANSLATIONS["article_page"]["listen_to_podcast"].get(lang, TRANSLATIONS["article_page"]["listen_to_podcast"]["it"])
            headset_icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-headphones"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h1a2 2 0 0 1 2 2v3z"></path><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v3z"></path></svg>"""
            podcast_button_html = f"""<button id="podcast-button" class="podcast-button" data-src="{article['audio_path']}">
                    {headset_icon_svg}
                    <span>{podcast_button_text}</span>
                </button>"""

        youtube_button_html = ""
        if article.get("youtube_url"):
            video_button_text = TRANSLATIONS["article_page"]["watch_video"].get(lang, TRANSLATIONS["article_page"]["watch_video"]["it"])
            youtube_icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-youtube"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2A29 29 0 0 0 23 11.75a29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>"""
            youtube_button_html = f"""<a href="{article['youtube_url']}" target="_blank" rel="noopener noreferrer" class="youtube-button">
                    {youtube_icon_svg}
                    <span>{video_button_text}</span>
                </a>"""

        if podcast_button_html or youtube_button_html:
            media_container_html = f"""
            <div class="media-controls">
                {podcast_button_html}
                {youtube_button_html}
            </div>
            <div id="media-player-container" style="display: none; margin-top: 15px;"></div>
            """

        article_view_html = f"""
        <div id="article-view">
            <h1>{article['title']}</h1>
            {author_html}
            {tags_html}
            {media_container_html}
            {article['html_content']}
            
            <div class="a2a_kit a2a_kit_size_32 a2a_default_style" style="margin-top: 30px; text-align: center;">
                <a class="a2a_button_facebook"></a>
                <a class="a2a_button_x"></a>
                <a class="a2a_button_pinterest"></a>
                <a class="a2a_button_email"></a>
                <a class="a2a_dd" href="https://www.addtoany.com/share"></a>
            </div>

            <div class="footer-back-button">
                {tags_html}
                <a href="#article-view" class="back-button" style="margin-top: 20px;">{back_to_top_button_text}</a>
            </div>
        </div>
        """

        temp_html = base_template.replace("{{content}}", article_view_html)
        temp_html = temp_html.replace("{{pagination_controls}}", "")
        
        page_title = f"{article['title']} - AITalk"
        meta_description = article['summary']
        og_url = f"{SITE_URL}{lang}/{article['path']}"
        og_image = ""
        if article.get('image_paths'):
             og_image = f"{SITE_URL}{lang}/{article['image_paths']['full_jpeg']}"
        else:
             og_image = f"{SITE_URL}logo_vn_ia.png"

        temp_html = temp_html.replace("{{page_title}}", page_title)
        temp_html = temp_html.replace("{{meta_description}}", meta_description)
        temp_html = temp_html.replace("{{og_url}}", og_url)
        temp_html = temp_html.replace("{{og_image}}", og_image)
        temp_html = temp_html.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">')

        temp_html = temp_html.replace("{{subtitle}}", TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"]))
        temp_html = temp_html.replace("{{subscribe_link_text}}", TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"]))
        temp_html = temp_html.replace("{{footer_curated_by}}", TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"]))
        temp_html = temp_html.replace("{{footer_contacts}}", TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"]))
        temp_html = temp_html.replace("{{footer_editorial_method}}", TRANSLATIONS["footer"]["editorial_method"].get(lang, TRANSLATIONS["footer"]["editorial_method"]["it"]))

        base_data = get_base_template_data(depth=1)
        for placeholder, path in base_data.items():
            temp_html = temp_html.replace(placeholder, path)
        
        dropdown_html = generate_language_dropdown_html(current_lang=lang, depth=1)
        temp_html = temp_html.replace("{{language_dropdown_html}}", dropdown_html)

        with open(os.path.join(output_dir, article['path']), "w", encoding='utf-8') as f:
            f.write(temp_html)


def generate_author_pages(authors_data, articles, output_dir, lang='it'):
    """
    Generates a standalone page for each author.
    """
    print("\nGenerating author pages...")
    if not authors_data:
        print("  - No authors found. Skipping.")
        return

    with open("templates/base.html", "r", encoding='utf-8') as f:
        base_template = f.read()
    with open("templates/author.html", "r", encoding='utf-8') as f:
        author_template = f.read()

    author_output_dir = os.path.join(output_dir, "authors")
    os.makedirs(author_output_dir, exist_ok=True)

    for slug, author in authors_data.items():
        print(f"  - Generating page for {author['name']}")

        author_articles = [p for p in articles if p.get('author') == author['name']]
        author_articles.sort(key=lambda p: p.get('date'), reverse=True)
        
        article_list_html = ""
        if author_articles:
            for article in author_articles[:10]:
                article_path = f"../{article['path']}"
                article_list_html += f'<a href="{article_path}" class="author-article-link">{article["title"]}</a>'
        else:
            article_list_html = f'<p>{TRANSLATIONS["author_page"]["no_articles_found"].get(lang, "No articles found for this author.")}</p>'

        links_html = ""
        if author.get('links'):
            for name, url in author['links'].items():
                links_html += f'<a href="{url}" target="_blank" rel="noopener noreferrer" class="author-social-link">{name.capitalize()}</a>'

        photo_tag = '<div class="author-placeholder-photo"></div>'
        if author.get('photo'):
            photo_paths = process_author_photo(author['photo'], BASE_OUTPUT_DIR, lang)
            if photo_paths:
                photo_tag = f"""
                <picture>
                    <source srcset="{photo_paths['webp']}" type="image/webp">
                    <source srcset="{photo_paths['jpeg']}" type="image/jpeg">
                    <img src="{photo_paths['jpeg']}" alt="{author['name']}" loading="lazy" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover;">
                </picture>
                """
        
        content_html = author_template.replace("{{author_name}}", author['name'])
        content_html = content_html.replace("{{author_photo_picture_tag}}", photo_tag)
        content_html = content_html.replace("{{author_links_html}}", links_html)
        content_html = content_html.replace("{{author_bio_html}}", author['bio'])
        content_html = content_html.replace("{{article_list_html}}", article_list_html)
        content_html = content_html.replace("{{back_button_text}}", TRANSLATIONS["article_page"]["back_button"].get(lang, "Go back"))
        content_html = content_html.replace("{{biography_title}}", TRANSLATIONS["author_page"]["biography"].get(lang, "Biography"))
        content_html = content_html.replace("{{latest_articles_title}}", TRANSLATIONS["author_page"]["latest_articles"].get(lang, "Latest Articles"))

        page_title_suffix = TRANSLATIONS["author_page"]["page_title_suffix"].get(lang, "Author at AITalk")
        page_title = f"{author['name']} - {page_title_suffix}"
        meta_description = BeautifulSoup(author['bio'], 'html.parser').get_text(strip=True)[:155]
        
        temp_html = base_template.replace("{{content}}", content_html)
        temp_html = temp_html.replace("{{page_title}}", page_title)
        temp_html = temp_html.replace("{{meta_description}}", meta_description)
        temp_html = temp_html.replace("{{subtitle}}", TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"]))
        temp_html = temp_html.replace("{{pagination_controls}}", "")
        temp_html = temp_html.replace("{{subscribe_link_text}}", TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"]))
        temp_html = temp_html.replace("{{footer_curated_by}}", TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"]))
        temp_html = temp_html.replace("{{footer_contacts}}", TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"]))
        temp_html = temp_html.replace("{{footer_editorial_method}}", TRANSLATIONS["footer"]["editorial_method"].get(lang, TRANSLATIONS["footer"]["editorial_method"]["it"]))

        base_data = get_base_template_data(depth=2)
        for placeholder, path in base_data.items():
            temp_html = temp_html.replace(placeholder, path)
        
        dropdown_html = generate_language_dropdown_html(current_lang=lang, depth=2)
        temp_html = temp_html.replace("{{language_dropdown_html}}", dropdown_html)

        og_url = f"{SITE_URL}{lang}/authors/{slug}.html"
        og_image = f"{SITE_URL}{lang}/{IMAGE_ASSETS_DIR}/authors/{os.path.basename(photo_paths['jpeg'])}" if author.get('photo') and photo_paths else f"{SITE_URL}logo_vn_ia.png"
        temp_html = temp_html.replace("{{og_url}}", og_url)
        temp_html = temp_html.replace("{{og_image}}", og_image)

        output_path = os.path.join(author_output_dir, f"{slug}.html")
        with open(output_path, "w", encoding='utf-8') as f:
            f.write(temp_html)


def generate_index_page(articles, output_dir, lang='it'):
    """
    Generates the index page with the first batch of articles and a JSON
    file for the rest to be loaded dynamically.
    """
    print("\nGenerating index page and JSON for dynamic loading...")
    with open("templates/base.html", "r", encoding='utf-8') as f:
        base_template = f.read()

    try:
        if lang == 'it': locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')
        elif lang == 'en': locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        elif lang == 'es': locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        elif lang == 'fr': locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        elif lang == 'de': locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
    except locale.Error:
        print(f"Locale for {lang} not supported, using default.")
        locale.setlocale(locale.LC_TIME, '')

    all_tags = sorted(list(set(tag for article in articles for tag in article.get('tags', []))))
    filter_bar_html = '<div id="tag-filter-bar" style="margin-bottom: 20px; text-align: center; flex-wrap: wrap; display: flex; justify-content: center; gap: 10px;">'
    filter_bar_html += '<button class="tag-filter-button active" data-tag="all">All</button>'
    for tag in all_tags:
        filter_bar_html += f'<button class="tag-filter-button" data-tag="{tag}">{tag}</button>'
    filter_bar_html += '</div>'

    ARTICLES_PER_PAGE = 15
    initial_articles = articles[:ARTICLES_PER_PAGE]
    
    grid_html = '<div id="articles-grid">\n'
    for article in initial_articles:
        date_html = ""
        if article.get('date'):
            formatted_date = article['date'].strftime('%d %B %Y')
            date_html = f'<p class="article-card-date">{formatted_date}</p>'

        tags_html = ""
        if article.get('tags'):
            tags_html = '<div class="article-card-tags">' + "".join([f'<span class="tag">{tag}</span>' for tag in article['tags']]) + '</div>'
        
        image_html = f'<img src="logo_vn_ia.png" alt="{article["title"]}" loading="lazy">'
        if article.get('image_paths'):
            paths = article['image_paths']
            image_html = f"""
                <picture>
                    <source srcset="{paths['thumb_webp']}" type="image/webp">
                    <source srcset="{paths['thumb_jpeg']}" type="image/jpeg">
                    <img src="{paths['thumb_jpeg']}" alt="{article['title']}" loading="lazy">
                </picture>
            """

        tags_data_attr = " ".join(article.get('tags', []))
        card_html = f"""
            <a href="{article['path']}" class="article-card" data-tags="{tags_data_attr}">
                {image_html}
                <div class="article-card-content">
                    {date_html}<h3>{article['title']}</h3><p>{article['summary']}</p>{tags_html}
                </div>
            </a>
            """
        grid_html += card_html
    grid_html += '</div>'

    json_output_path = os.path.join(output_dir, "articles.json")
    serializable_articles = []
    for article in articles:
        article_copy = article.copy()
        if isinstance(article_copy.get('date'), (datetime, date)):
            article_copy['date'] = article_copy['date'].isoformat()
        serializable_articles.append(article_copy)

    with open(json_output_path, "w", encoding='utf-8') as f:
        json.dump(serializable_articles, f, ensure_ascii=False)
    print(f"  - Generated articles.json with {len(articles)} articles.")

    pagination_html = '<div id="view-more-container"></div>' if len(articles) > ARTICLES_PER_PAGE else ''
    
    articles_heading_text = TRANSLATIONS["index_page"]["articles_heading"].get(lang, TRANSLATIONS["index_page"]["articles_heading"]["it"])
    articles_heading_html = f'<h2 class="visually-hidden">{articles_heading_text}</h2>'
    content_with_filter = filter_bar_html + articles_heading_html + grid_html
    temp_html = base_template.replace("{{content}}", content_with_filter)
    temp_html = temp_html.replace("{{pagination_controls}}", pagination_html)

    subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
    temp_html = temp_html.replace("{{subtitle}}", subtitle)
    temp_html = temp_html.replace("{{subscribe_link_text}}", TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"]))
    temp_html = temp_html.replace("{{footer_curated_by}}", TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"]))
    temp_html = temp_html.replace("{{footer_contacts}}", TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"]))
    temp_html = temp_html.replace("{{footer_editorial_method}}", TRANSLATIONS["footer"]["editorial_method"].get(lang, TRANSLATIONS["footer"]["editorial_method"]["it"]))

    base_data = get_base_template_data(depth=1)
    for placeholder, path in base_data.items():
        temp_html = temp_html.replace(placeholder, path)
    
    dropdown_html = generate_language_dropdown_html(current_lang=lang, depth=1)
    temp_html = temp_html.replace("{{language_dropdown_html}}", dropdown_html)

    view_more_text = TRANSLATIONS["pagination"]["view_more"].get(lang, TRANSLATIONS["pagination"]["view_more"]["it"])
    temp_html = temp_html.replace("{{lang}}", lang)
    temp_html = temp_html.replace("{{view_more_text}}", view_more_text.replace("'", "\\'"))

    page_title = f"AITalk - {subtitle}"
    temp_html = temp_html.replace("{{page_title}}", page_title)
    temp_html = temp_html.replace("{{meta_description}}", subtitle)
    temp_html = temp_html.replace("{{og_url}}", f"{SITE_URL}{lang}/index.html")
    temp_html = temp_html.replace("{{og_image}}", f"{SITE_URL}logo_vn_ia.png")

    with open(os.path.join(output_dir, "index.html"), "w", encoding='utf-8') as f:
        f.write(temp_html)

def generate_local_pages(output_dir, lang='it'):
    """
    Generates standalone pages from the /pages directory.
    """
    local_pages_meta = {
        "newsletter.html": {"title": TRANSLATIONS["newsletter_page"]["title"], "description": TRANSLATIONS["newsletter_page"]["description"]},
        "thank-you.html": {"title": TRANSLATIONS["thank_you_page"]["title"], "description": TRANSLATIONS["thank_you_page"]["paragraph"]},
        "cookie.html": {"title": TRANSLATIONS["cookie_page"]["title"], "description": TRANSLATIONS["cookie_page"]["p1"]},
        "privacy.html": {"title": TRANSLATIONS["privacy_page"]["title"], "description": TRANSLATIONS["privacy_page"]["p1"]},
        "metodo-editoriale.html": {"title": TRANSLATIONS["metodo_page"]["title"], "description": TRANSLATIONS["metodo_page"]["p1"]}
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

            final_content = page_content
            # Replace placeholders in the page content itself
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
            if filename == "metodo-editoriale.html":
                for key, trans_dict in TRANSLATIONS["metodo_page"].items():
                    placeholder = f"{{{{metodo_page_{key}}}}}"
                    translation = trans_dict.get(lang, trans_dict["it"])
                    final_content = final_content.replace(placeholder, translation)
            
            thank_you_link = f"/{lang}/thank-you.html"
            final_content = final_content.replace("{{thank_you_link}}", thank_you_link)

            soup = BeautifulSoup(final_content, 'html.parser')
            form = soup.find('form', {'name': 'newsletter'})
            if form:
                form_name = f"newsletter-{lang}"
                form['name'] = form_name
                if not form.find('input', {'name': 'form-name'}):
                    form_name_input = soup.new_tag('input', attrs={'type': 'hidden', 'name': 'form-name', 'value': form_name})
                    form.append(form_name_input)
                if filename == "newsletter.html" and not form.find('input', {'name': 'language'}):
                    hidden_input = soup.new_tag('input', attrs={'type': 'hidden', 'name': 'language', 'value': lang})
                    form.append(hidden_input)
                final_content = str(soup)
            
            # Replace placeholders in the base template
            temp_html = base_template.replace("{{content}}", final_content)
            temp_html = temp_html.replace("{{pagination_controls}}", "")
            
            # SEO
            subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
            meta_info = local_pages_meta.get(filename, {"title": {"it": "AITalk"}, "description": {"it": subtitle}})
            page_title = f"{meta_info['title'].get(lang, meta_info['title']['it'])} - AITalk"
            meta_description = meta_info['description'].get(lang, meta_info['description']['it'])
            og_url = f"{SITE_URL}{lang}/{filename}"
            og_image = f"{SITE_URL}logo_vn_ia.png" # Use the main logo
            temp_html = temp_html.replace("{{page_title}}", page_title)
            temp_html = temp_html.replace("{{meta_description}}", meta_description)
            temp_html = temp_html.replace("{{og_url}}", og_url)
            temp_html = temp_html.replace("{{og_image}}", og_image)
            
            temp_html = temp_html.replace("{{subtitle}}", TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"]))
            temp_html = temp_html.replace("{{subscribe_link_text}}", TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"]))
            temp_html = temp_html.replace("{{footer_curated_by}}", TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"]))
            temp_html = temp_html.replace("{{footer_contacts}}", TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"]))
            temp_html = temp_html.replace("{{footer_editorial_method}}", TRANSLATIONS["footer"]["editorial_method"].get(lang, TRANSLATIONS["footer"]["editorial_method"]["it"]))
            
            base_data = get_base_template_data(depth=1)
            for placeholder, path in base_data.items():
                temp_html = temp_html.replace(placeholder, path)
            
            dropdown_html = generate_language_dropdown_html(current_lang=lang, depth=1)
            temp_html = temp_html.replace("{{language_dropdown_html}}", dropdown_html)

            with open(os.path.join(output_dir, filename), "w", encoding='utf-8') as f:
                f.write(temp_html)

def generate_404_page(output_dir, lang='it'):
    """
    Generates a 404.html page for the given language.
    """
    print(f"\nGenerating 404 page for language: '{lang}'...")
    try:
        with open("templates/base.html", "r", encoding='utf-8') as f:
            base_template = f.read()
        with open("templates/404.html", "r", encoding='utf-8') as f:
            not_found_content = f.read()

        # Translate the content of the 404 page itself
        for key, trans_dict in TRANSLATIONS["not_found_page"].items():
            placeholder = f"{{{{not_found_page_{key}}}}}"
            translation = trans_dict.get(lang, trans_dict["it"])
            not_found_content = not_found_content.replace(placeholder, translation)

        # Inject the 404 content into the base template
        temp_html = base_template.replace("{{content}}", not_found_content)
        temp_html = temp_html.replace("{{pagination_controls}}", "") # No pagination on 404 page

        # Set up translations and paths for the base template
        subtitle = TRANSLATIONS["subtitle"].get(lang, TRANSLATIONS["subtitle"]["it"])
        temp_html = temp_html.replace("{{subtitle}}", subtitle)
        temp_html = temp_html.replace("{{subscribe_link_text}}", TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"]))
        temp_html = temp_html.replace("{{footer_curated_by}}", TRANSLATIONS["footer"]["curated_by"].get(lang, TRANSLATIONS["footer"]["curated_by"]["it"]))
        temp_html = temp_html.replace("{{footer_contacts}}", TRANSLATIONS["footer"]["contacts"].get(lang, TRANSLATIONS["footer"]["contacts"]["it"]))
        temp_html = temp_html.replace("{{footer_editorial_method}}", TRANSLATIONS["footer"]["editorial_method"].get(lang, TRANSLATIONS["footer"]["editorial_method"]["it"]))

        # SEO and metadata
        meta_info = TRANSLATIONS["not_found_page"]
        page_title = f"{meta_info['title'].get(lang, meta_info['title']['it'])} - AITalk"
        meta_description = meta_info['paragraph'].get(lang, meta_info['paragraph']['it'])
        og_url = f"{SITE_URL}{lang}/404.html"
        og_image = f"{SITE_URL}logo_vn_ia.png" # Use the main logo

        temp_html = temp_html.replace("{{page_title}}", page_title)
        temp_html = temp_html.replace("{{meta_description}}", meta_description)
        temp_html = temp_html.replace("{{og_url}}", og_url)
        temp_html = temp_html.replace("{{og_image}}", og_image)

        # Asset paths (depth is 1, as it's in the root of the lang folder)
        base_data = get_base_template_data(depth=1)
        for placeholder, path in base_data.items():
            temp_html = temp_html.replace(placeholder, path)
        
        dropdown_html = generate_language_dropdown_html(current_lang=lang, depth=1)
        temp_html = temp_html.replace("{{language_dropdown_html}}", dropdown_html)

        # Write the final file
        output_path = os.path.join(output_dir, "404.html")
        with open(output_path, "w", encoding='utf-8') as f:
            f.write(temp_html)
        print(f"  - Generated 404.html for '{lang}'")

    except FileNotFoundError as e:
        print(f"  - ERROR: Could not generate 404 page. Missing template file: {e.filename}")
        raise
    except Exception as e:
        print(f"  - ERROR: An unexpected error occurred while generating the 404 page: {e}")
        raise

def copy_static_assets(output_dir):
    """
    Copies static assets from the root and the public directory to the output directory.
    """
    print("\nCopying static assets...")
    
    # Copy root files
    static_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.css', '.js', '.html', '.webp', '.ico']
    for item in os.listdir('.'):
        if os.path.isfile(item) and any(item.endswith(ext) for ext in static_extensions):
            if item not in ["base.html", "forms.html"]:
                print(f"  - {item}")
                shutil.copy(item, os.path.join(output_dir, item))

    # Copy public directory contents recursively
    public_dir = 'public'
    if os.path.exists(public_dir):
        print(f"  - Copying '{public_dir}' directory...")
        shutil.copytree(public_dir, output_dir, dirs_exist_ok=True)

def generate_rss_feed(articles, output_dir, lang='it'):
    """
    Generates an RSS feed from the list of articles.
    """
    print("\nGenerating RSS feed...")
    fg = FeedGenerator()
    
    rss_title = TRANSLATIONS["rss"]["title"].get(lang, TRANSLATIONS["rss"]["title"]["it"])
    rss_description = TRANSLATIONS["rss"]["description"].get(lang, TRANSLATIONS["rss"]["description"]["it"])

    fg.title(f"{rss_title} ({lang})")
    fg.link(href=f"{SITE_URL}{lang}/", rel='alternate')
    fg.link(href=f"{SITE_URL}{lang}/rss.xml", rel='self')
    fg.description(rss_description)
    fg.language(lang)
    fg.generator('AITalk.it')

    for article in reversed(articles):
        fe = fg.add_entry()
        fe.title(article['title'])
        full_url = f"{SITE_URL}{lang}/{article['path']}"
        fe.link(href=full_url)
        fe.description(article['summary'])
        fe.guid(full_url, permalink=True)

        pub_date_val = article.get('date')
        if isinstance(pub_date_val, (datetime, date)):
            dt_obj = pub_date_val
            if isinstance(dt_obj, date) and not isinstance(dt_obj, datetime):
                dt_obj = datetime.combine(dt_obj, datetime.min.time())
            
            if dt_obj.tzinfo is None:
                dt_obj = dt_obj.replace(tzinfo=timezone.utc)
            fe.pubDate(dt_obj)

        if article.get('image_paths'):
            enclosure_url = f"{SITE_URL}{lang}/{article['image_paths']['full_jpeg']}"
            fe.enclosure(url=enclosure_url, length='0', type='image/jpeg')
            
    fg.rss_file(os.path.join(output_dir, 'rss.xml'), pretty=True)
    print(f"  - rss.xml (for {lang})")

def generate_sitemap_xml():
    print("\nGenerating sitemap.xml...")
    articles_db = get_local_articles_db()
    urls = []
    for lang in LANGUAGES:
        urls.append(f"{SITE_URL}{lang}/")

    for article_dir, languages in articles_db.items():
        for lang, files in languages.items():
            for file_info in files:
                slug = os.path.splitext(file_info['name'])[0].strip().replace('_', '-')
                path = f"{slug}.html"
                encoded_path = quote(path)
                urls.append(f"{SITE_URL}{lang}/{encoded_path}")

    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sorted(urls):
        xml_content += f"  <url>\n    <loc>{url}</loc>\n  </url>\n"
    xml_content += '</urlset>'

    with open(os.path.join(BASE_OUTPUT_DIR, "sitemap.xml"), "w", encoding='utf-8') as f:
        f.write(xml_content)
    print(f"  - sitemap.xml generated with {len(urls)} URLs.")


def generate_robots_txt():
    print("\nGenerating robots.txt...")
    content = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_URL}sitemap.xml"
    )
    with open(os.path.join(BASE_OUTPUT_DIR, "robots.txt"), "w", encoding='utf-8') as f:
        f.write(content)
    print("  - robots.txt generated.")


if __name__ == "__main__":
    main()
