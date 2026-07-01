#!/usr/bin/env python3
"""Instala localmente os modelos oficiais de português normal e best."""

from __future__ import annotations

import re
import shutil
import subprocess
import os
import tempfile
import urllib.request
from pathlib import Path


MODELOS = {
    ".tessdata_fast": "https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/por.traineddata",
    ".tessdata_best": "https://raw.githubusercontent.com/tesseract-ocr/tessdata_best/main/por.traineddata",
}


def localizar_tessdata() -> Path:
    executavel = shutil.which("tesseract")
    if not executavel:
        raise RuntimeError("Tesseract não encontrado no PATH.")
    resultado = subprocess.run(
        [executavel, "--list-langs"], capture_output=True, text=True, errors="replace", check=True
    )
    texto = resultado.stdout + resultado.stderr
    encontrado = re.search(r"languages in ([^\n]+?)/?\s*\(", texto)
    if encontrado:
        candidato = Path(encontrado.group(1).strip().strip('"'))
        if candidato.is_dir():
            return candidato

    # Alguns pacotes omitem o caminho na saída de --list-langs.
    raiz_executavel = Path(executavel).resolve().parent
    candidatos = [
        Path(os.environ.get("TESSDATA_PREFIX", "")),
        raiz_executavel / "tessdata",  # Windows/UB-Mannheim
        raiz_executavel.parent / "share" / "tessdata",  # Homebrew
        Path("/usr/share/tessdata"),
        Path("/usr/local/share/tessdata"),
    ]
    candidatos.extend(Path("/usr/share/tesseract-ocr").glob("*/tessdata"))
    for candidato in candidatos:
        if candidato.is_dir() and (candidato / "osd.traineddata").is_file():
            return candidato
    raise RuntimeError("Não foi possível localizar a pasta tessdata do Tesseract.")


def main() -> None:
    origem = localizar_tessdata()
    raiz = Path(__file__).resolve().parent
    for pasta, url in MODELOS.items():
        destino = raiz / pasta
        destino.mkdir(exist_ok=True)
        # Copia OSD e configurações exigidas pelo OCRmyPDF.
        shutil.copytree(origem, destino, dirs_exist_ok=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".traineddata") as temporario:
            temporario_path = Path(temporario.name)
        try:
            print(f"Baixando o modelo português {pasta.removeprefix('.tessdata_')}...")
            with urllib.request.urlopen(url, timeout=60) as resposta:
                with temporario_path.open("wb") as arquivo:
                    shutil.copyfileobj(resposta, arquivo)
            if temporario_path.stat().st_size < 1_000_000:
                raise RuntimeError("O modelo baixado parece estar incompleto.")
            temporario_path.replace(destino / "por.traineddata")
            (destino / ".installed").write_text("tesseract/por\n", encoding="utf-8")
        finally:
            temporario_path.unlink(missing_ok=True)
        print(f"Modelo instalado em: {destino}")


if __name__ == "__main__":
    main()
