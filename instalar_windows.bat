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
where tesseract >nul 2>nul || goto instalar_tesseract
goto tesseract_ok

:instalar_tesseract
echo Instalando o mecanismo de reconhecimento de texto...
winget install -e --id UB-Mannheim.TesseractOCR
echo Feche esta janela e execute este instalador novamente para concluir.
pause
exit /b 0

:tesseract_ok
uv python install 3.12
uv venv --python 3.12 .venv
uv pip install --python ".venv\Scripts\python.exe" -r requirements-windows.txt
if errorlevel 1 goto erro
".venv\Scripts\python.exe" instalar_modelo_best.py
if errorlevel 1 goto erro
echo Instalação concluída. Execute abrir_acervo_ocr.bat.
pause
exit /b 0

:erro
echo Não foi possível concluir a instalação. Verifique as mensagens acima.
pause
exit /b 1
