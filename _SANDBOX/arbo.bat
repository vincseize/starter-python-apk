@echo off
chcp 65001 >nul
REM Se placer dans le dossier du .bat
cd /d "%~dp0"

REM Lancement du script Python arbo.py
python arbo.py

REM Fermer la console si tout s'est bien passe, sinon rester ouverte
if errorlevel 1 (
    echo.
    echo Une erreur s'est produite.
    pause
)