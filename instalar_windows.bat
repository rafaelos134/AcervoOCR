@echo off
chcp 65001 >nul
cd /d "%~dp0"
where uv >nul 2>nul || goto instalar_uv
goto uv_ok

:instalar_uv
  echo Instalando uv...
  winget install -e --id astral-sh.uv
  echo Feche esta janela e execute este instalador novamente.
  pause
  exit /b 0

:uv_ok
where tesseract >nul 2>nul || (
  echo Instalando Tesseract. Marque o idioma Portuguese durante a instalação, se solicitado.
  winget install -e --id UB-Mannheim.TesseractOCR
)
echo Instalando Python 3.12 e as bibliotecas...
uv python install 3.12
uv venv --python 3.12 .venv
uv pip install --python ".venv\Scripts\python.exe" -r requirements.txt
if errorlevel 1 (
  echo A instalação falhou. Verifique as mensagens acima.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" instalar_modelo_best.py
if errorlevel 1 (
  echo Não foi possível instalar o modelo de alta qualidade. Feche esta janela e execute o instalador novamente.
  pause
  exit /b 1
)
echo.
echo Instalação concluída. Abra executar_windows.bat ou arraste PDFs sobre ele.
pause
