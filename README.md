# AITalk: Motore per Sito Statico e Repository dei Contenuti

[![Stato Deployment](https://img.shields.io/github/actions/workflow/status/darioferrero/aitalk/deploy.yml?branch=main&label=Deploy)](https://github.com/darioferrero/aitalk/actions)
[![Tecnologia](https://img.shields.io/badge/Motore-Python%20SSG-blue.svg)](https://www.python.org/)
[![Piattaforma](https://img.shields.io/badge/Piattaforma-Netlify-00ad9f.svg)](https://www.netlify.com/)

AITalk è un generatore di siti statici (SSG) professionale ad alte prestazioni, specificamente progettato per portali di notizie multilingua focalizzati sull'Intelligenza Artificiale. Questa repository contiene il codice sorgente completo, gli script di automazione e il database dei contenuti in formato Markdown.

---

## 🚀 Funzionalità Principali

### ⚡ Prestazioni e Architettura
- **SSG in Pure Python**: Motore di build personalizzato (`build.py`) progettato per la massima velocità e il minimo sovraccarico.
- **Build Incrementali Atomiche**: Il rilevamento intelligente dei cambiamenti tramite hashing SHA-1 garantisce che solo i contenuti modificati vengano rielaborati.
- **Elaborazione Parallela**: Utilizza `ProcessPoolExecutor` per la generazione ultra-veloce delle pagine HTML su più core della CPU.

### 🌐 Eccellenza Multilingua
- **Supporto Nativo**: Esperienza completamente localizzata per **Italiano**, **Inglese**, **Spagnolo**, **Francese** e **Tedesco**.
- **Ricerca Live**: Motore di ricerca integrato lato client ad alta velocità, con filtraggio per lingua e risoluzione dinamica dei percorsi.
- **Ottimizzazione SEO**: Feed RSS specifici per lingua, generazione automatica di robots.txt e metadati OpenGraph/Twitter corretti per ogni pagina.

### 🎙️ Multimedia e Engagement
- **Integrazione Podcast**: Rilevamento e integrazione automatica di file audio (`.mp3`) specifici per lingua con player HTML5 nativo.
- **Embed YouTube**: Supporto integrato per i contenuti video all'interno degli articoli.
- **Motore E-Book**: Script specializzati per compilare gli articoli Markdown in e-book professionali nei formati PDF/EPUB.
- **Automazione Newsletter**: Sistema di iscrizione alla newsletter serverless tramite Netlify Forms.

### 📊 Analisi e Insight
- **Tracciamento Privacy-First**: Monitoraggio leggero delle visualizzazioni di pagina senza cookie, tramite Netlify Functions e Netlify Blobs.
- **Dashboard Prestazioni**: Monitoraggio delle statistiche in tempo reale senza tracker di terze parti.

---

## 📂 Struttura del Progetto

```text
├── articoli/           # Database principale (Markdown + Media)
├── content/            # Dati ausiliari (Biografie e profili autori)
├── ebook/              # Suite per la generazione di E-book
├── netlify/            # Funzioni serverless (Statistiche, Analytics)
├── pages/              # Pagine informative statiche (Legali, Cookie, Metodo)
├── templates/          # Template HTML (Base, Articolo, Autore, 404)
├── public/             # Asset statici (Bandiere, icone, loghi)
├── build.py            # Motore SSG principale
├── build.sh            # Automazione globale della build
└── style.css           # Sistema di design globale
```

---

## 🛠️ Flusso di Lavoro per lo Sviluppo

### Prerequisiti
- **Python 3.10+**
- **pip** (Python Package Manager)

### Configurazione Locale
1. Clona la repository.
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

### Sistema di Build
- **Build Completa (Tutte le lingue)**:
  ```bash
  ./build.sh
  ```
- **Build Mirata**:
  ```bash
  python build.py --lang [it|en|es|fr|de]
  ```

### Anteprima Locale
Avvia un server web locale per ispezionare il sito generato nella cartella `dist/`:
```bash
cd dist
python -m http.server 8000
```
Accedi al portale all'indirizzo: `http://localhost:8000`

---

## 📝 Gestione dei Contenuti

### Articoli
Ogni articolo risiede nella propria directory all'interno di `articoli/`, identificato da un prefisso numerico per l'ordinamento cronologico (es. `105-slug/`).
- **Traduzioni**: Aggiungi il suffisso del codice lingua ai file (es. `articolo_en.md`).
- **Media**: Inserisci immagini e file audio direttamente nella cartella dell'articolo. Il motore gestisce automaticamente l'ottimizzazione e la conversione dei formati (WebP/JPEG).

### Autori
Gestisci i profili degli autori in `content/authors/`. I dati biografici supportano la formattazione completa in Markdown.

---

## ☁️ Deployment e CI/CD
Il portale viene distribuito automaticamente tramite **GitHub Actions**. Ogni push sul ramo main avvia una build automatica e il deployment su **Netlify**. Il workflow utilizza strategie di caching avanzate per garantire tempi di distribuzione rapidi.

---
© 2025 AITalk - A cura di **Dario Ferrero**
