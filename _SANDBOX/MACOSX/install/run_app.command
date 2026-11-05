#!/bin/bash
cd "$(dirname "$0")"
echo "Starter Python APK - Lancement"
python3 run.py
status=$?
echo
read -r -p "Appuyez sur Entrée pour fermer..."
exit "$status"
