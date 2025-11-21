@echo off
setlocal

REM --- Impostazione del Contesto di Esecuzione ---
REM Cambia la directory corrente in quella in cui si trova lo script.
REM Questo garantisce che tutti i percorsi relativi siano sempre corretti.
cd /d "%~dp0"

REM --- Configurazione dell'Ambiente ---
set VENV_DIR=%cd%\ebook_env

echo --- Controllo dell'Ambiente Virtuale ---

REM Controlla se Python 3 è installato
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Errore: Python 3 non sembra essere installato o aggiunto al PATH.
    pause
    exit /b 1
)

REM Crea l'ambiente virtuale se non esiste
if not exist "%VENV_DIR%" (
    echo Creazione di un nuovo ambiente virtuale in '%VENV_DIR%'...
    python -m venv "%VENV_DIR%"
    if %errorlevel% neq 0 (
        echo ERRORE CRITICO: Creazione dell'ambiente virtuale fallita.
        pause
        exit /b 1
    )
)

REM --- Esecuzione dello Script ---
echo Attivazione dell'ambiente virtuale...
call "%VENV_DIR%\Scripts\activate.bat"

echo.
echo Controllo e installazione delle dipendenze...
python -m pip install -r "requirements.txt"
if %errorlevel% neq 0 (
    echo ERRORE CRITICO: Installazione delle dipendenze fallita.
    pause
    exit /b 1
)

echo.
REM Richiede l'input dell'utente
set /p start_num="Inserisci il numero della cartella di partenza: "
set /p end_num="Inserisci il numero della cartella di fine: "

echo.
echo Avvio della generazione dell'ebook...
python "ebook_generator.py" %start_num% %end_num%

echo.
echo Operazione completata.
pause
