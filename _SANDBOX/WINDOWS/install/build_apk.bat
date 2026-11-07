```bat
@echo off
setlocal

title Build Android APK

echo.
echo ==========================================
echo       BUILD ANDROID - PYTHON / FLET
echo ==========================================
echo.

REM Racine du projet
set "PROJECT_ROOT=%~dp0..\..\.."
for %%I in ("%PROJECT_ROOT%") do set "PROJECT_ROOT=%%~fI"

REM Script Python de compilation
set "BUILD_SCRIPT=%~dp0build.py"

REM Dossier de sortie Flet
set "APK_DIR=%PROJECT_ROOT%\src\build\apk"

echo Projet : %PROJECT_ROOT%
echo.
echo Lancement de la compilation...
echo.

if not exist "%BUILD_SCRIPT%" (
    echo ERREUR : build.py introuvable.
    pause
    exit /b 1
)

REM Compilation
py -3 "%BUILD_SCRIPT%"

if errorlevel 1 (
    echo.
    echo ERREUR : la compilation a echoue.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo       COMPILATION TERMINEE !
echo ==========================================
echo.

REM Vérification du dossier APK
if exist "%APK_DIR%" (
    echo Ouverture du dossier APK :
    echo %APK_DIR%
    start "" explorer.exe "%APK_DIR%"
) else (
    echo ATTENTION : dossier APK introuvable.
    echo Recherche dans les sorties Flutter...

    set "APK_DIR=%PROJECT_ROOT%\src\build\flutter\build\app\outputs\apk\release"

    if exist "%APK_DIR%" (
        start "" explorer.exe "%APK_DIR%"
    ) else (
        echo Aucun dossier APK trouve.
    )
)

echo.
pause
exit /b 0
```