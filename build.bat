@echo off
ECHO Questo script installera' le dipendenze necessarie e costruira' il sito web.
ECHO Assicurati di avere Python e pip installati e aggiunti al PATH di sistema.
ECHO.
PAUSE

ECHO Installazione delle dipendenze da requirements.txt...
pip install -r requirements.txt

IF %ERRORLEVEL% NEQ 0 (
    ECHO Si e' verificato un errore durante l'installazione delle dipendenze.
    PAUSE
    EXIT /B %ERRORLEVEL%
)

ECHO.
ECHO Avvio del processo di build per tutte le lingue...
ECHO.

FOR %%L IN (it en es fr de) DO (
    ECHO --- Costruzione del sito per la lingua: %%L ---
    python build.py --lang %%L
    IF %ERRORLEVEL% NEQ 0 (
        ECHO Si e' verificato un errore durante la costruzione per la lingua %%L.
        PAUSE
        EXIT /B %ERRORLEVEL%
    )
    ECHO.
)

ECHO --- Generazione dei file master (sitemap, robots.txt)... ---
python build.py --master-files
IF %ERRORLEVEL% NEQ 0 (
    ECHO Si e' verificato un errore durante la generazione dei file master.
    PAUSE
    EXIT /B %ERRORLEVEL%
)

ECHO.
ECHO Processo di build completato con successo!
PAUSE
