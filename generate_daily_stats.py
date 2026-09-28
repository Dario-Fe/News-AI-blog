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

# Quanti path elencare nel dettaglio delle anomalie (i conteggi totali sono sempre completi)
ANOMALY_LIMIT = 25
# Un path mai visto prima con piu' visite di queste e' sospetto (blob ricreato o rinominato)
NEW_PATH_VIEWS_ALERT = 50
# Quota del contatore persa oltre la quale si sospetta un azzeramento completo dello store
STORE_WIPE_SHARE = 0.2

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
                    spotify_url = post.metadata.get('spotify') or post.metadata.get('spotify_url')
                    
                    has_podcast = bool(spotify_url) or (md_basename in mp3_names)
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


def fetch_stats_summary():
    """
    Fetches the current cumulative page views and the data-quality block
    detected by the hourly aggregator (update-stats.mjs) from the Netlify Function.

    Returns a tuple (cumulative_views, summary_quality).
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

        # Anomalie rilevate dal riepilogo orario: contatori tornati indietro,
        # path spariti, blob illeggibili, incrementi non registrati.
        # Servono solo a documentare; non modificano le visite conteggiate.
        summary_quality = data.get("dataQuality") or {}
        
        # Converte la lista di [{path, count}] in un dizionario {path: count}
        cumulative = {}
        for item in data.get("statsData", []):
            path = item["path"]
            # Pulisce il path rimuovendo slash iniziale/finale per uniformità
            clean_path = path.strip("/")
            cumulative[clean_path] = item["count"]
            
        return cumulative, summary_quality
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
                "top_articles": {},
                # Visite che il contatore ha perso nel mese (anomalie, non filtrate)
                "dropped_views": 0,
                # Valore del contatore cumulativo a fine mese
                "counter_total": None
            }
        
        m = monthly[month_str]
        m["total_views"] += day_data.get("total_views", 0)
        m["dropped_views"] += (day_data.get("data_quality") or {}).get("lost_views", 0)
        if day_data.get("counter_total") is not None:
            m["counter_total"] = day_data["counter_total"]
        
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
                "views_by_tag": {},
                "dropped_views": 0,
                "counter_total": None
            }
            
        y = yearly[year_str]
        y["total_views"] += day_data.get("total_views", 0)
        y["dropped_views"] += (day_data.get("data_quality") or {}).get("lost_views", 0)
        if day_data.get("counter_total") is not None:
            y["counter_total"] = day_data["counter_total"]
        
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
    current_cumulative, summary_quality = fetch_stats_summary()

    # 3. Scansiona gli articoli locali per mappare i tag e recuperare lo snapshot statico
    article_mapping, portal_snapshot = scan_local_articles()

    # 4. Calcola la differenza (delta / incrementi) del giorno
    total_views = 0
    views_by_lang = {}
    views_by_tag = {}
    detailed_views = {}

    # Anomalie del contatore rilevate durante il calcolo del delta del giorno
    regressions = []            # path il cui contatore e' tornato indietro
    suspicious_new_paths = []   # path nuovi con un conteggio sospettosamente alto

    previous_last_update = history.get("last_update")
    current_total = sum(current_cumulative.values())
    previous_total = history.get("cumulative_total") or sum(previous_cumulative.values())

    for path, count in current_cumulative.items():
        # Calcola l'incremento rispetto all'ultimo tracciamento memorizzato
        if path in previous_cumulative:
            prev_count = previous_cumulative[path]
            increment = count - prev_count

            # Contatore tornato indietro (reset di un blob): si annota il calo e
            # NON si conteggia nulla. Il vecchio "increment = count" regalava al
            # giorno l'intero valore del contatore, gonfiando lo storico con
            # visite gia' registrate nei giorni precedenti.
            if increment < 0:
                regressions.append({
                    "path": path,
                    "from": prev_count,
                    "to": count,
                    "lost": -increment,
                })
                increment = 0
        else:
            # Path mai visto prima: le visite sono genuinamente nuove.
            increment = count
            if count > NEW_PATH_VIEWS_ALERT:
                suspicious_new_paths.append({"path": path, "views": count})

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

    # 5-bis. Qualita' del contatore: cali, path spariti, visite non registrate.
    # Questi valori NON modificano le visite del giorno: documentano cosa il
    # contatore ha perso, cosi' l'anomalia resta visibile invece di sparire
    # dentro il delta giornaliero.
    run_at = datetime.now(timezone.utc)
    net_change = current_total - previous_total
    regressions_count = len(regressions)
    lost_views = sum(item["lost"] for item in regressions)
    dropped_writes_by_day = summary_quality.get("droppedWrites") or {}
    dropped_writes_day = dropped_writes_by_day.get(target_date_str, 0)
    hourly_regressions = summary_quality.get("regressions") or []
    missing_paths = summary_quality.get("missing") or []
    unreadable_paths = summary_quality.get("unreadable") or []

    warnings = []
    if regressions_count:
        warnings.append(
            f"Contatore tornato indietro su {regressions_count} path ({lost_views} visite perse): probabile reset di un blob."
        )
    if previous_total and lost_views > STORE_WIPE_SHARE * previous_total:
        warnings.append(
            f"Perse oltre il {int(STORE_WIPE_SHARE * 100)}% delle visite del contatore ({lost_views} su {previous_total}): sospetto azzeramento completo dello store."
        )
    if dropped_writes_day:
        warnings.append(
            f"{dropped_writes_day} visite non registrate da page-view.mjs (conflitti di scrittura)."
        )
    if unreadable_paths:
        warnings.append(
            f"{len(unreadable_paths)} contatori illeggibili: conservato l'ultimo valore noto."
        )
    if missing_paths:
        warnings.append(f"{len(missing_paths)} path spariti dal contatore.")
    if suspicious_new_paths:
        warnings.append(
            f"{len(suspicious_new_paths)} path nuovi con visite anomale (possibile blob ricreato o rinominato)."
        )
    if total_views != net_change:
        warnings.append(
            f"Il totale del giorno ({total_views}) non coincide con la variazione del contatore ({net_change})."
        )
    for warning in warnings:
        print(f"  ! Qualita' dati: {warning}")

    # 5. Salva i dati della giornata sotto lo storico daily
    # Se per quel giorno non ci sono state visite, impostiamo comunque la giornata vuota per continuità
    history["historical"]["daily"][target_date_str] = {
        "total_views": total_views,
        "views_by_lang": views_by_lang,
        "views_by_tag": views_by_tag,
        "top_articles": sorted_top_day,
        "detailed_views": detailed_views,
        # Controllo: valore del contatore cumulativo al momento dello snapshot
        "counter_total": current_total,
        # Finestra temporale effettivamente coperta dal giorno (il job gira
        # quando GitHub lo esegue, non a mezzanotte: vedi AGENTS della wiki)
        "window_start": previous_last_update,
        "window_end": run_at.isoformat(),
        "data_quality": {
            "lost_views": lost_views,
            "regressions": regressions[:ANOMALY_LIMIT],
            "regressions_count": regressions_count,
            "hourly_regressions": hourly_regressions[:ANOMALY_LIMIT],
            "dropped_writes": dropped_writes_day,
            "missing_paths": missing_paths,
            "unreadable_paths": unreadable_paths,
            "suspicious_new_paths": suspicious_new_paths,
            "counter_before": previous_total,
            "counter_after": current_total,
            "net_change": net_change,
            "warnings": warnings,
        },
    }

    # 6. Aggiorna lo snapshot del portale e il riferimento cumulativo per la prossima esecuzione
    history["last_update"] = run_at.isoformat()
    history["portal_snapshot"] = portal_snapshot
    history["cumulative_history"] = current_cumulative
    # Totali di controllo: permettono di verificare in qualsiasi momento che la
    # somma dei delta giornalieri coincida con la variazione del contatore.
    history["cumulative_total"] = current_total
    history["previous_cumulative_total"] = previous_total
    history["dropped_writes_by_day"] = dropped_writes_by_day

    # 7. Ricalcola le aggregazioni mensili e annuali complessive
    update_aggregates(history)

    # 8. Scrittura del file finale nel repository
    save_history(history)


if __name__ == "__main__":
    main()
