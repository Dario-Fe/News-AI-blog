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
        "privacy.html": {"title": TRANSLATIONS["privacy_page"]["title"], "description": TRANSLATIONS["privacy_page"]["p1"]}
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
