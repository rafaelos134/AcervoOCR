@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo O programa ainda não foi instalado. Execute instalar_windows.bat primeiro.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" pdf_ocr.py %*
if errorlevel 1 pause
