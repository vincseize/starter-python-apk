@echo off
setlocal
cd /d "%~dp0"
title Starter Python APK - Build APK
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 build.py
) else (
    python build.py
)
if errorlevel 1 echo La compilation a echoue. Consultez les messages ci-dessus.
echo.
pause
