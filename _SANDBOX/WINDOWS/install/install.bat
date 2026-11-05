@echo off
setlocal
cd /d "%~dp0"
title Starter Python APK - Installation
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 install.py
) else (
    python install.py
)
if errorlevel 1 (
    echo.
    echo Installation interrompue. Consultez le message d'erreur ci-dessus.
) 
echo.
pause
