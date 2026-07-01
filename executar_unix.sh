#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "Execute ./instalar_unix.sh primeiro."
  exit 1
fi
exec .venv/bin/python pdf_ocr.py "$@"
