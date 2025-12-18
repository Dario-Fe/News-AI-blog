#!/bin/bash
echo "Questo script installerà le dipendenze necessarie e costruirà il sito web."
read -p "Premi Invio per continuare..."

echo "Installazione delle dipendenze da requirements.txt..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Si è verificato un errore durante l'installazione delle dipendenze."
    read -p "Premi Invio per uscire."
    exit 1
fi

echo ""
echo "Avvio del processo di build per tutte le lingue..."
echo ""

LANGUAGES=("it" "en" "es" "fr" "de")

for lang in "${LANGUAGES[@]}"; do
    echo "--- Costruzione del sito per la lingua: $lang ---"
    python3 build.py --lang "$lang"
    if [ $? -ne 0 ]; then
        echo "Si è verificato un errore durante la costruzione per la lingua $lang."
        read -p "Premi Invio per uscire."
        exit 1
    fi
    echo ""
done

echo "--- Generazione dei file master (sitemap, robots.txt)... ---"
python3 build.py --master-files
if [ $? -ne 0 ]; then
    echo "Si è verificato un errore during la generazione dei file master."
    read -p "Premi Invio per uscire."
    exit 1
fi

echo ""
echo "Processo di build completato con successo!"
read -p "Premi Invio per uscire."
