# Notizie IA - Static Site Generator

Questa repository contiene il codice sorgente per il sito web di Notizie IA, un'applicazione web moderna e performante costruita come generatore di sito statico (Static Site Generator - SSG).

Il sito recupera dinamicamente gli articoli dal repository [CorsoAIBook](https://github.com/matteobaccan/CorsoAIBook) durante un processo di build e genera un sito HTML statico, veloce e multilingua.

## Core Technologies
- **Python**: Per la logica di build principale.
- **Static Site Generation (SSG)**: Per la massima performance e affidabilità.
- **GitHub Actions**: Per l'automazione del processo di build e deployment (CI/CD).
- **Netlify**: Piattaforma di hosting e gestione form "serverless".

## Struttura del Progetto
```
.
├── .github/workflows/      # Configurazione di GitHub Actions per il CI/CD
├── dist/                   # Cartella di output del sito generato (non versionata)
├── pages/                  # Pagine HTML locali (es. newsletter) da includere nel build
├── templates/              # Contiene il template base (base.html)
├── build.py                # Lo script Python principale che contiene la logica di build
├── build.sh                # Lo script shell che orchestra l'intero processo di build
├── requirements.txt        # Le dipendenze Python del progetto
├── README.md               # Questo file
└── ...                     # Altri file statici (logo, etc.)
```

## Come Funziona: Il Processo di Build
Il sito viene generato tramite lo script `build.sh`, che esegue i seguenti passaggi:

1.  **Pulizia**: Cancella la cartella `dist/` per assicurare un build pulito.
2.  **Copia Asset Statici**: Copia tutti i file statici (immagini, CSS, JS, e file HTML statici come `thank-you.html`) dalla root del progetto alla cartella `dist/`.
3.  **Build Multilingua**: Esegue un ciclo per ogni lingua supportata (`it`, `en`, `es`, `fr`, `de`). Per ogni lingua:
    a. **Recupera Articoli**: Contatta le API di GitHub per scaricare gli ultimi articoli dal repository esterno.
    b. **Genera Pagine Articoli**: Crea una pagina HTML per ogni singolo articolo.
    c. **Genera Pagine Locali**: Crea pagine HTML basate sui file presenti nella cartella `pages/` (es. `newsletter.html`).
    d. **Genera Pagine Indice**: Crea la pagina `index.html` per la lingua corrente, con la lista di tutti gli articoli.
    e. **Genera Feed RSS**: Crea un file `rss.xml` per la lingua corrente.
4.  **Crea Redirect Principale**: Genera il file `index.html` nella root di `dist/` che reindirizza automaticamente alla versione italiana del sito.

## Funzionalità Principali
- **Generazione di Sito Statico**: Il sito è pre-renderizzato in file HTML, garantendo velocità di caricamento massime per l'utente finale.
- **Supporto Multilingua Completo**: Il sito è generato in Italiano, Inglese, Spagnolo, Francese e Tedesco. L'interfaccia, inclusi i link, i sottotitoli e le pagine, è completamente tradotta grazie a un sistema di traduzione centralizzato in `build.py`.
- **Form per Newsletter (Netlify-Ready)**: Include una pagina di iscrizione alla newsletter con un form HTML pronto per essere gestito da Netlify Forms, eliminando la necessità di un backend dedicato.
- **Build e Deployment Automatizzati**: Grazie a GitHub Actions, il sito viene ricostruito e pubblicato automaticamente due volte al giorno per recuperare i nuovi articoli e ad ogni modifica del codice sorgente.

## Sviluppo Locale
Per eseguire il progetto in locale, segui questi passaggi.

**Prerequisiti**:
- Python 3.x

**Installazione**:
1. Clona la repository.
2. Installa le dipendenze Python:
   ```bash
   pip install -r requirements.txt
   ```

**Esecuzione del Build**:
Per generare il sito nella cartella `dist/`, esegui:
```bash
./build.sh
```

**Visualizzazione**:
Per visualizzare il sito generato, puoi avviare un semplice server web locale dalla cartella `dist`:
```bash
cd dist
python -m http.server
```
Il sito sarà quindi accessibile all'indirizzo `http://localhost:8000`.

## Deployment
Il deployment è gestito automaticamente da GitHub Actions. Il workflow è configurato per la pubblicazione su **Netlify**. È necessario configurare il progetto su Netlify per usare il comando di build `./build.sh` e la cartella di pubblicazione `dist`.
