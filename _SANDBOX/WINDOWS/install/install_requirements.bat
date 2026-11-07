@echo off
CHCP 65001 > nul
TITLE Installation des dépendances Python

echo ===================================================
echo   Installation des dépendances du projet
echo ===================================================
echo.

:: Définition du dossier racine du projet (deux niveaux au-dessus si placé dans _SANDBOX\WINDOWS\install)
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

:: Recherche du script Python à lancer
if exist "install_requirements.py" (
    set "PYTHON_SCRIPT=install_requirements.py"
) else if exist "install.py" (
    set "PYTHON_SCRIPT=install.py"
) else (
    echo [ERREUR] Aucun script d'installation Python n'a été trouvé.
    pause
    exit /b 1
)

:: Exécution via l'interpréteur Python
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py %PYTHON_SCRIPT%
) else (
    where python >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        python %PYTHON_SCRIPT%
    ) else (
        echo [ERREUR] Python n'est pas installé ou accessible dans le PATH.
        pause
        exit /b 1
    )
)

echo.
echo ===================================================
echo   Opération terminée avec succès.
echo ===================================================
pause