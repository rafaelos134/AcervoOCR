#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"

if command -v brew >/dev/null 2>&1; then
  brew install tesseract tesseract-lang
elif command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y curl tesseract-ocr tesseract-ocr-por tesseract-ocr-eng
elif command -v dnf >/dev/null 2>&1; then
  sudo dnf install -y curl tesseract tesseract-langpack-por tesseract-langpack-eng
else
  echo "Gerenciador não reconhecido. Instale Tesseract e os idiomas por/eng."
  exit 1
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "Instalando uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  if [ -f "$HOME/.local/bin/env" ]; then
    . "$HOME/.local/bin/env"
  else
    PATH="$HOME/.local/bin:$PATH"
    export PATH
  fi
fi

uv python install 3.12
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python instalar_modelo_best.py
echo "Instalação concluída. Execute: ./executar_unix.sh"
