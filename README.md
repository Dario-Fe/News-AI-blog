# AITalk - Generatore di Sito Statico

Questa repository contiene il codice sorgente e lo script di build per il sito di AITalk, un sito web statico e multilingua dedicato a notizie e analisi sull'Intelligenza Artificiale.

Il sito recupera dinamicamente gli articoli dal repository [CorsoAIBook](https://github.com/matteobaccan/CorsoAIBook) durante il processo di build e genera un sito HTML statico, veloce e performante.

## Funzionalità Principali

- **Generazione di Sito Statico**: Costruito con un semplice script Python (`build.py`), senza la necessità di framework complessi, per garantire massime performance.
- **Contenuti in Markdown**: Gli articoli sono scritti in formato Markdown, rendendo la gestione dei contenuti semplice e intuitiva.
- **Supporto Multilingua**: Il sito è generato in Italiano (default), Inglese, Spagnolo, Francese e Tedesco. L'interfaccia e i template sono completamente tradotti.
- **Pagine Autore**: Genera automaticamente una pagina dedicata per ogni autore con biografia e lista degli articoli pubblicati.
- **Integrazione Podcast**: Rileva e integra automaticamente file audio `.mp3` specifici per ogni lingua, mostrando un player dedicato nelle pagine degli articoli.
- **Ottimizzazione Immagini**: Scarica e processa le immagini degli articoli, creando formati ottimizzati (WebP e JPEG) per migliorare i tempi di caricamento.
- **Feed RSS**: Genera un feed RSS separato per ogni lingua, per permettere agli utenti di seguire gli aggiornamenti.
- **Form "Serverless"**: Utilizza Netlify Forms per la gestione delle iscrizioni alla newsletter, senza bisogno di un backend.

## Struttura del Progetto

- `build.py`: Lo script Python principale che contiene tutta la logica di build.
- `build.sh`: Uno script di supporto per avviare la compilazione di tutte le lingue con un solo comando.
- `content/`: Contiene i dati che non risiedono nel repository esterno degli articoli.
  - `authors/`: File Markdown con le biografie degli autori (es. `dario-ferrero.md`, `dario-ferrero_en.md`).
- `templates/`: Contiene i template HTML per la struttura delle pagine (es. `base.html`, `author.html`).
- `pages/`: Contiene pagine HTML quasi-statiche come la privacy policy e la pagina di iscrizione alla newsletter.
- `public/`: Contiene asset statici (come immagini e font) che vengono copiati direttamente nella cartella di build.
  - `flags/`: Immagini SVG delle bandiere per il selettore della lingua.
- `style.css`: Il foglio di stile principale del sito.
- `requirements.txt`: Le dipendenze Python necessarie per eseguire lo script di build.
- `dist/`: La cartella di output dove viene salvato il sito generato (non è tracciata da Git).
- **Contenuti Articoli**: I contenuti principali (articoli, immagini associate e podcast) vengono recuperati dalla cartella `articoli/` del repository [matteobaccan/CorsoAIBook](https://github.com/matteobaccan/CorsoAIBook).

## Gestione dei Contenuti

### Articoli

Per aggiungere o modificare un articolo, è necessario creare o modificare i file nel repository `CorsoAIBook`. Ogni articolo deve avere una propria cartella all'interno della directory `articoli/`.
- **File Markdown**: Il file per la lingua italiana non ha suffisso (es. `mio-articolo.md`). Le traduzioni devono avere il suffisso della lingua (es. `mio-articolo_en.md` per l'inglese).
- **Immagini**: Le immagini relative a un articolo vanno inserite nella stessa cartella.

### Podcast

Per associare un podcast a un articolo, inserire un file `.mp3` nella stessa cartella dell'articolo nel repository `CorsoAIBook`. Il file audio **deve avere lo stesso nome base** del file Markdown a cui si riferisce.
- Per `mio-articolo.md` (Italiano), il file audio deve chiamarsi `mio-articolo.mp3`.
- Per `mio-articolo_en.md` (Inglese), il file audio deve chiamarsi `mio-articolo_en.mp3`.

Lo script di build rileverà automaticamente il file audio e mostrerà il player nella pagina dell'articolo corrispondente.

### Autori

Per aggiungere o modificare un autore, creare o modificare i file Markdown presenti nella cartella `content/authors/` di questa repository.

## Sviluppo e Build in Locale

### Prerequisiti

- Python 3.x
- `pip`

### Setup

1.  Clonare la repository.
2.  Installare le dipendenze Python:
    ```bash
    pip install -r requirements.txt
    ```
3.  (Opzionale ma Raccomandato) Per evitare di raggiungere i limiti di richieste alle API di GitHub, è consigliabile creare un [Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) con scope `repo` ed esportarlo come variabile d'ambiente:
    ```bash
    export GITHUB_TOKEN='tuo_token_qui'
    ```

### Esecuzione del Build

Per compilare il sito per tutte le lingue supportate, eseguire lo script:
```bash
./build.sh
```
Per compilare una singola lingua (es. italiano):
```bash
python build.py --lang it
```
Il sito generato si troverà nella cartella `dist/`.

### Visualizzazione in Locale

Per visualizzare il sito generato, è possibile avviare un semplice server web locale dalla cartella `dist/`:
```bash
cd dist
python -m http.server
```
Il sito sarà quindi accessibile all'indirizzo `http://localhost:8000`.

## Deployment

Il deployment è gestito automaticamente tramite GitHub Actions e avviene su Netlify.
