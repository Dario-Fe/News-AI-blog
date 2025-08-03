# Notizie IA - Web App

Questa è una web app semplice e auto-contenuta, creata per visualizzare gli articoli del repository [CorsoAIBook](https://github.com/matteobaccan/CorsoAIBook) in un formato blog user-friendly.

## Descrizione

La web app, intitolata **"Notizie IA"** e presentata "A cura di Verbania Notizie", è interamente contenuta nel singolo file `index.html`. È stata progettata per essere leggera e non richiedere un backend o un processo di build.

## Come Funziona

L'applicazione utilizza JavaScript per interagire con l'API pubblica di GitHub e caricare dinamicamente i contenuti. Al caricamento della pagina:

1.  **Recupera gli Articoli**: Effettua una chiamata all'API di GitHub per elencare tutte le cartelle presenti nella directory `/articoli` del repository.
2.  **Ordinamento Dinamico**: Le cartelle e gli articoli in più parti vengono ordinati per mostrare sempre i più recenti in cima alla lista.
3.  **Genera le Schede**: Per ogni articolo (o parte di articolo) trovato, genera una scheda di anteprima sulla pagina principale. Questa scheda include:
    *   Il titolo dell'articolo.
    *   Un'immagine di copertina (la prima immagine trovata nel file Markdown).
    *   Un breve sommario (il primo paragrafo di testo dopo l'immagine).
4.  **Visualizzazione Articolo**: Cliccando su una scheda, l'utente può visualizzare l'articolo completo. Il contenuto del file `.md` corrispondente viene caricato, convertito in HTML al volo (usando la libreria `marked.js`), e visualizzato in una pagina di lettura pulita.

## Caratteristiche Principali

-   **Single-File Application**: Tutta la logica, gli stili e la struttura sono contenuti in `index.html`.
-   **Zero Dipendenze di Build**: Funziona direttamente in un browser web senza necessità di compilazione o installazione di pacchetti.
-   **Contenuti Dinamici**: Nuovi articoli o nuove parti di articoli aggiunti alla cartella `/articoli` appariranno automaticamente nell'app al successivo caricamento (dopo la scadenza della cache di sessione).
-   **Caching Intelligente**: Utilizza `sessionStorage` per memorizzare nella cache l'elenco degli articoli per un'ora, riducendo le chiamate all'API di GitHub e migliorando i tempi di caricamento.
-   **Design Responsivo**: L'interfaccia si adatta a diverse dimensioni di schermo, dai desktop ai dispositivi mobili.

## Utilizzo

Per utilizzare l'applicazione, è sufficiente aprire il file `index.html` in un qualsiasi browser web moderno.
