#!/bin/bash
cd "$(dirname "$0")"
echo "Starter Python APK - Compilation APK"
python3 build.py
status=$?
echo
read -r -p "Appuyez sur Entrée pour fermer..."
exit "$status"
