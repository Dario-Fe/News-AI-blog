# AITalk - Generatore di Sito Statico

Questa repository contiene il codice sorgente e lo script di build per il sito di AITalk, un sito web statico e multilingua dedicato a notizie e analisi sull'Intelligenza Artificiale.

A differenza delle versioni precedenti, questo generatore ora opera interamente in locale, leggendo i contenuti dalla cartella `articoli/` presente in questa stessa repository.

## Funzionalità Principali

- **Generazione di Sito Statico**: Costruito con un semplice script Python (`build.py`), senza la necessità di framework complessi, per garantire massime performance e semplicità.
- **Contenuti Locali in Markdown**: Gli articoli sono scritti in formato Markdown e gestiti direttamente all'interno del progetto, rendendo la gestione dei contenuti semplice e versionabile con Git.
- **Supporto Multilingua**: Il sito è generato in Italiano (default), Inglese, Spagnolo, Francese e Tedesco. L'interfaccia e i template sono completamente tradotti.
- **Build Stabili**: Le dipendenze Python nel file `requirements.txt` sono "pinnate" a versioni specifiche, garantendo che la build sia riproducibile e non si rompa a causa di aggiornamenti inaspettati delle librerie.
- **Pagine Autore**: Genera automaticamente una pagina dedicata per ogni autore con biografia e lista degli articoli pubblicati.
- **Integrazione Podcast**: Rileva e integra automaticamente file audio `.mp3` specifici per ogni lingua, mostrando un player dedicato nelle pagine degli articoli.
- **Ottimizzazione Immagini**: Processa le immagini degli articoli, creando formati ottimizzati (WebP e JPEG) per migliorare i tempi di caricamento.
- **Feed RSS**: Genera un feed RSS separato per ogni lingua, per permettere agli utenti di seguire gli aggiornamenti.
- **Form "Serverless"**: Utilizza Netlify Forms per la gestione delle iscrizioni alla newsletter, senza bisogno di un backend.

## Struttura del Progetto

- `build.py`: Lo script Python principale che contiene tutta la logica di build.
- `build.sh`: Uno script di supporto per avviare la compilazione di tutte le lingue con un solo comando.
- `articoli/`: La cartella principale che contiene tutti i contenuti degli articoli (file markdown, immagini, audio).
- `content/`: Contiene i dati ausiliari.
  - `authors/`: File Markdown con le biografie degli autori (es. `dario-ferrero.md`, `dario-ferrero_en.md`).
- `templates/`: Contiene i template HTML per la struttura delle pagine (es. `base.html`, `author.html`).
- `pages/`: Contiene pagine HTML quasi-statiche come la privacy policy e la pagina di iscrizione alla newsletter.
- `public/`: Contiene asset statici (come le bandiere delle lingue) che vengono copiati direttamente nella cartella di build.
- `style.css`: Il foglio di stile principale del sito.
- `requirements.txt`: Le dipendenze Python necessarie per eseguire lo script di build.
- `dist/`: La cartella di output dove viene salvato il sito generato (non è tracciata da Git).

## Gestione dei Contenuti

### Articoli

Per aggiungere o modificare un articolo, è necessario creare una nuova sottocartella all'interno di `articoli/`.
- **File Markdown**: Il file per la lingua italiana non ha suffisso (es. `mio-articolo.md`). Le traduzioni devono avere il suffisso della lingua (es. `mio-articolo_en.md` per l'inglese).
- **Immagini**: Le immagini relative a un articolo vanno inserite nella stessa cartella.

### Podcast

Per associare un podcast a un articolo, inserire un file `.mp3` nella stessa cartella dell'articolo. Il file audio **deve avere lo stesso nome base** del file Markdown a cui si riferisce.
- Per `mio-articolo.md` (Italiano), il file audio deve chiamarsi `mio-articolo.mp3`.
- Per `mio-articolo_en.md` (Inglese), il file audio deve chiamarsi `mio-articolo_en.mp3`.

Lo script di build rileverà automaticamente il file audio e mostrerà il player nella pagina dell'articolo corrispondente.

### Autori

Per aggiungere o modificare un autore, creare o modificare i file Markdown presenti nella cartella `content/authors/`.

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
    Non è più necessario un token di GitHub, poiché tutti i contenuti sono locali.

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
