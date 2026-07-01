@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\pythonw.exe" (
  echo Execute instalar_windows.bat primeiro.
  pause
  exit /b 1
)
start "" ".venv\Scripts\pythonw.exe" acervo_ocr_gui.py
