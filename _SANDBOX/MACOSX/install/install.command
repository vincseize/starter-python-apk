#!/bin/bash
cd "$(dirname "$0")"
echo "Starter Python APK - Installation macOS"
echo
if command -v python3 >/dev/null 2>&1; then
  python3 install.py
else
  echo "ERREUR : Python 3 est introuvable. Installez Python 3 puis recommencez."
  exit 1
fi
status=$?
echo
read -r -p "Appuyez sur Entrée pour fermer..."
exit "$status"
