$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    throw "Instale o uv antes de compilar: https://docs.astral.sh/uv/"
}
if (-not (Get-Command tesseract -ErrorAction SilentlyContinue)) {
    throw "Instale o Tesseract 64 bits antes de compilar."
}

uv python install 3.12
uv venv --python 3.12 .venv-build
uv pip install --python .venv-build\Scripts\python.exe -r requirements-build.txt
& .venv-build\Scripts\python.exe instalar_modelo_best.py
& .venv-build\Scripts\pyinstaller.exe --noconfirm --clean AcervoOCR.spec

$TesseractExe = (Get-Command tesseract).Source
$TesseractDir = Split-Path $TesseractExe
Copy-Item $TesseractDir dist\AcervoOCR\tesseract -Recurse -Force

$Inno = "${env:ProgramFiles(x86)}\Inno Setup 6\ISCC.exe"
if (-not (Test-Path $Inno)) {
    throw "Instale o Inno Setup 6 antes de gerar o instalador."
}
& $Inno instalador_windows.iss
Write-Host "Instalador criado em dist\installer" -ForegroundColor Green
