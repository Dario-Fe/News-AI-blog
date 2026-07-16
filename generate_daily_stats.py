#!/usr/bin/env python3
import os
import sys
import json
import re
import requests
from datetime import datetime, timedelta, timezone
import frontmatter

# Constants
STATS_URL = "https://aitalk.it/.netlify/functions/stats?format=json"
HISTORY_FILE_PATH = "public/stats_history.json"
ARTICLES_DIR = "articoli"

def scan_local_articles():
    """
    Scans the local 'articoli' directory and builds a database of articles,
    mapping their relative URL path to tags, language, title, and media presence.
    Also returns global portal metadata.
    """
    article_mapping = {}
    
    total_articles = 0
    articles_by_lang = {"it": 0, "en": 0, "es": 0, "fr": 0, "de": 0}
    total_words_by_lang = {"it": 0, "en": 0, "es": 0, "fr": 0, "de": 0}
    podcast_articles_count = 0
    video_articles_count = 0
    tags_popularity = {}
    unique_authors = set()

    if not os.path.exists(ARTICLES_DIR):
        print(f"Directory {ARTICLES_DIR} non trovata.")
        return article_mapping, {}

    for root, _, files in os.walk(ARTICLES_DIR):
        if root == ARTICLES_DIR:
            continue
        
        # Cerca i file mp3 per i podcast
        mp3_names = {os.path.splitext(f)[0] for f in files if f.endswith('.mp3')}

        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                try:
                    post = frontmatter.load(filepath)
                    md_basename = os.path.splitext(filename)[0]
                    
                    # Riconoscimento lingua
                    lang = 'it'
                    if md_basename.endswith('_en'): lang = 'en'
                    elif md_basename.endswith('_es'): lang = 'es'
                    elif md_basename.endswith('_fr'): lang = 'fr'
                    elif md_basename.endswith('_de'): lang = 'de'

                    # Calcolo slug dell'articolo (con e senza suffisso lingua per massima robustezza)
                    slug = md_basename.strip().replace('_', '-')
                    path_key = f"{lang}/{slug}.html"

                    # Slug senza suffisso di lingua
                    slug_no_lang = md_basename
                    for suffix in ['_en', '_es', '_fr', '_de']:
                        if slug_no_lang.endswith(suffix):
                            slug_no_lang = slug_no_lang[:-len(suffix)]
                            break
                    slug_no_lang = slug_no_lang.strip().replace('_', '-')
                    path_key_no_lang = f"{lang}/{slug_no_lang}.html"

                    # Dati e Metadati
                    title = post.content.split('\n')[0].replace('#', '').strip() if post.content else "Senza titolo"
                    tags = post.metadata.get('tags', [])
                    author = post.metadata.get('author')
                    youtube_url = post.metadata.get('youtube_url')
                    
                    has_podcast = md_basename in mp3_names
                    has_video = bool(youtube_url)

                    # Conteggio parole
                    words_count = len(re.findall(r'\w+', post.content)) if post.content else 0

                    # Mapping per associare il path alle informazioni dell'articolo
                    info = {
                        "title": title,
                        "tags": tags,
                        "lang": lang,
                        "author": author,
                        "has_podcast": has_podcast,
                        "has_video": has_video
                    }
                    
                    # Registra tutte le varianti di percorsi possibili per massima tolleranza
                    article_mapping[path_key] = info
                    article_mapping[f"/{path_key}"] = info
                    article_mapping[path_key_no_lang] = info
                    article_mapping[f"/{path_key_no_lang}"] = info

                    # Aggregazioni Portale
                    total_articles += 1
                    if lang in articles_by_lang:
                        articles_by_lang[lang] += 1
                        total_words_by_lang[lang] += words_count
                    else:
                        articles_by_lang[lang] = 1
                        total_words_by_lang[lang] = words_count

                    if has_podcast:
                        podcast_articles_count += 1
                    if has_video:
                        video_articles_count += 1
                    
                    if author:
                        unique_authors.add(author)

                    for tag in tags:
                        tags_popularity[tag] = tags_popularity.get(tag, 0) + 1

                except Exception as e:
                    print(f"Errore nella lettura dell'articolo {filepath}: {e}")

    portal_snapshot = {
        "total_articles": total_articles,
        "articles_by_lang": articles_by_lang,
        "total_words_by_lang": total_words_by_lang,
        "total_authors": len(unique_authors),
        "total_tags": len(tags_popularity),
        "tags_popularity": tags_popularity,
        "podcast_articles_count": podcast_articles_count,
        "video_articles_count": video_articles_count
    }

    return article_mapping, portal_snapshot


def fetch_cumulative_views():
    """
    Fetches the current cumulative page views from the Netlify Function.
    """
    user = os.environ.get("STATS_USER")
    password = os.environ.get("STATS_PASSWORD")

    if not user or not password:
        print("Errore: STATS_USER e STATS_PASSWORD devono essere impostati nelle variabili d'ambiente.")
        sys.exit(1)

    try:
        response = requests.get(STATS_URL, auth=(user, password), timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Converte la lista di [{path, count}] in un dizionario {path: count}
        cumulative = {}
        for item in data.get("statsData", []):
            path = item["path"]
            # Pulisce il path rimuovendo slash iniziale/finale per uniformità
            clean_path = path.strip("/")
            cumulative[clean_path] = item["count"]
            
        return cumulative
    except Exception as e:
        print(f"Errore nel recupero delle statistiche cumulative: {e}")
        sys.exit(1)


def load_history():
    """
    Loads the current history JSON from public/stats_history.json.
    Creates a new template structure if the file does not exist.
    """
    if os.path.exists(HISTORY_FILE_PATH):
        try:
            with open(HISTORY_FILE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Impossibile leggere lo storico esistente ({e}), ne creerò uno nuovo.")
            
    return {
        "last_update": None,
        "portal_snapshot": {},
        "cumulative_history": {},
        "historical": {
            "daily": {},
            "monthly": {},
            "yearly": {}
        }
    }


def save_history(history):
    """
    Saves the history JSON back to public/stats_history.json.
    """
    os.makedirs(os.path.dirname(HISTORY_FILE_PATH), exist_ok=True)
    with open(HISTORY_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
    print(f"Storico salvato con successo in {HISTORY_FILE_PATH}")


def update_aggregates(history):
    """
    Re-aggregates daily historical entries into monthly and yearly statistics
    to prevent calculation drift.
    """
    daily = history["historical"]["daily"]
    monthly = {}
    yearly = {}

    for date_str, day_data in sorted(daily.items()):
        # Extract Month (YYYY-MM) and Year (YYYY)
        month_str = date_str[:7]
        year_str = date_str[:4]

        # 1. Monthly Aggregation
        if month_str not in monthly:
            monthly[month_str] = {
                "total_views": 0,
                "views_by_lang": {},
                "views_by_tag": {},
                "top_articles": {}
            }
        
        m = monthly[month_str]
        m["total_views"] += day_data.get("total_views", 0)
        
        # Views by Lang
        for lang, count in day_data.get("views_by_lang", {}).items():
            m["views_by_lang"][lang] = m["views_by_lang"].get(lang, 0) + count
            
        # Views by Tag
        for tag, count in day_data.get("views_by_tag", {}).items():
            m["views_by_tag"][tag] = m["views_by_tag"].get(tag, 0) + count
            
        # Top Articles accumulating inside the month
        for path, count in day_data.get("detailed_views", {}).items():
            # Filtriamo solo articoli veri e propri (es. it/nome-articolo.html)
            if "/" in path and not path.endswith("index.html") and not path.endswith("404.html") and not path.endswith("newsletter.html"):
                m["top_articles"][path] = m["top_articles"].get(path, 0) + count

        # 2. Yearly Aggregation
        if year_str not in yearly:
            yearly[year_str] = {
                "total_views": 0,
                "views_by_lang": {},
                "views_by_tag": {}
            }
            
        y = yearly[year_str]
        y["total_views"] += day_data.get("total_views", 0)
        
        # Views by Lang
        for lang, count in day_data.get("views_by_lang", {}).items():
            y["views_by_lang"][lang] = y["views_by_lang"].get(lang, 0) + count
            
        # Views by Tag
        for tag, count in day_data.get("views_by_tag", {}).items():
            y["views_by_tag"][tag] = y["views_by_tag"].get(tag, 0) + count

    # Formatta i top_articles del mese in una lista ordinata
    for m_str, m_data in monthly.items():
        sorted_top = sorted(
            [{"path": path, "views": views} for path, views in m_data["top_articles"].items()],
            key=lambda x: x["views"],
            reverse=True
        )[:10] # Top 10 più visti del mese
        m_data["top_articles"] = sorted_top

    history["historical"]["monthly"] = monthly
    history["historical"]["yearly"] = yearly


def main():
    # Consente di forzare una data specifica via riga di comando per backfill o test
    target_date_str = None
    if len(sys.argv) > 1:
        target_date_str = sys.argv[1]
        # Validazione formato YYYY-MM-DD
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', target_date_str):
            print("Errore: la data deve essere nel formato YYYY-MM-DD")
            sys.exit(1)
    else:
        # Di default, elaboriamo la giornata di ieri (giorno appena concluso)
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        target_date_str = yesterday.strftime('%Y-%m-%d')

    print(f"Avvio elaborazione statistiche per il giorno: {target_date_str}")

    # 1. Carica lo storico esistente
    history = load_history()
    previous_cumulative = history.get("cumulative_history", {})

    # 2. Recupera le visualizzazioni cumulative correnti da Netlify
    current_cumulative = fetch_cumulative_views()

    # 3. Scansiona gli articoli locali per mappare i tag e recuperare lo snapshot statico
    article_mapping, portal_snapshot = scan_local_articles()

    # 4. Calcola la differenza (delta / incrementi) del giorno
    total_views = 0
    views_by_lang = {}
    views_by_tag = {}
    detailed_views = {}

    for path, count in current_cumulative.items():
        # Calcola l'incremento rispetto all'ultimo tracciamento memorizzato
        prev_count = previous_cumulative.get(path, 0)
        increment = count - prev_count

        # Gestisce un eventuale reset manuale dei contatori del server
        if increment < 0:
            increment = count

        if increment > 0:
            total_views += increment
            detailed_views[path] = increment

            # Determina la lingua del percorso
            # Se inizia con en/, es/, fr/, de/ è della lingua corrispondente, altrimenti default 'it'
            lang = 'it'
            for l in ['en', 'es', 'fr', 'de']:
                if path.startswith(f"{l}/"):
                    lang = l
                    break
            
            views_by_lang[lang] = views_by_lang.get(lang, 0) + increment

            # Associa i tag se si tratta di un articolo conosciuto
            article_info = article_mapping.get(path) or article_mapping.get(f"/{path}")
            if article_info and article_info.get("tags"):
                for tag in article_info["tags"]:
                    views_by_tag[tag] = views_by_tag.get(tag, 0) + increment

    # Trova i top 5 articoli più letti della giornata
    sorted_top_day = sorted(
        [{"path": path, "views": views} for path, views in detailed_views.items() if "/" in path and not path.endswith("index.html")],
        key=lambda x: x["views"],
        reverse=True
    )[:5]

    # 5. Salva i dati della giornata sotto lo storico daily
    # Se per quel giorno non ci sono state visite, impostiamo comunque la giornata vuota per continuità
    history["historical"]["daily"][target_date_str] = {
        "total_views": total_views,
        "views_by_lang": views_by_lang,
        "views_by_tag": views_by_tag,
        "top_articles": sorted_top_day,
        "detailed_views": detailed_views
    }

    # 6. Aggiorna lo snapshot del portale e il riferimento cumulativo per la prossima esecuzione
    history["last_update"] = datetime.now(timezone.utc).isoformat()
    history["portal_snapshot"] = portal_snapshot
    history["cumulative_history"] = current_cumulative

    # 7. Ricalcola le aggregazioni mensili e annuali complessive
    update_aggregates(history)

    # 8. Scrittura del file finale nel repository
    save_history(history)


if __name__ == "__main__":
    main()
