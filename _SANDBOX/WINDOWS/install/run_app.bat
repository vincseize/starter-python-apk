@echo off
setlocal
cd /d "%~dp0"
title Starter Python APK - Run
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 run.py
) else (
    python run.py
)
if errorlevel 1 echo L'application s'est arretee avec une erreur.
echo.
pause
