#!/bin/bash

# --- Configurazione dell'Ambiente ---
# Trova il percorso assoluto dello script
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
# Definisce il nome della cartella per l'ambiente virtuale
VENV_DIR="$SCRIPT_DIR/ebook_env"

echo "--- Controllo dell'Ambiente Virtuale ---"

# Controlla se python3 è installato
if ! command -v python3 &> /dev/null
then
    echo "Errore: python3 non sembra essere installato. Per favore, installalo."
    exit 1
fi

# Crea l'ambiente virtuale se non esiste
if [ ! -d "$VENV_DIR" ]; then
    echo "Creazione di un nuovo ambiente virtuale in '$VENV_DIR'..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "ERRORE CRITICO: Creazione dell'ambiente virtuale fallita."
        exit 1
    fi
fi

# --- Esecuzione dello Script ---
echo "Attivazione dell'ambiente virtuale..."
source "$VENV_DIR/bin/activate"

echo
echo "Controllo e installazione delle dipendenze nell'ambiente virtuale..."
python -m pip install -r "$SCRIPT_DIR/ebook/requirements.txt"
if [ $? -ne 0 ]; then
    echo "ERRORE CRITICO: Installazione delle dipendenze fallita."
    # Disattiva l'ambiente prima di uscire
    deactivate
    exit 1
fi

echo
# Richiede l'input dell'utente
echo -n "Inserisci il numero della cartella di partenza: "
read start_num
echo -n "Inserisci il numero della cartella di fine: "
read end_num

echo
echo "Avvio della generazione dell'ebook..."
python "$SCRIPT_DIR/ebook/ebook_generator.py" "$start_num" "$end_num"

echo
echo "Operazione completata. L'ambiente virtuale e' ancora attivo."
echo "Per disattivarlo, chiudi questo terminale o esegui 'deactivate'."
