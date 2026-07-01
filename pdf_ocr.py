#!/usr/bin/env python3
"""Converte PDFs digitalizados em PDFs pesquisáveis com OCR em português."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Adiciona OCR em português a um ou mais PDFs.",
    )
    p.add_argument("arquivos", nargs="*", type=Path, help="PDFs de entrada")
    p.add_argument("--forcar", action="store_true", help="refazer OCR inclusive em páginas que já têm texto")
    p.add_argument("--somente-portugues", action="store_true", help=argparse.SUPPRESS)
    p.add_argument(
        "--qualidade_alta",
        dest="qualidade_alta",
        action="store_true",
        help="usa alta qualidade (já é o padrão)",
    )
    p.add_argument(
        "--modo_rapido",
        dest="qualidade_alta",
        action="store_false",
        help="usa o modelo mais rápido em vez do modelo de alta qualidade",
    )
    p.add_argument("--texto", action="store_true", help="criar também um arquivo .txt com o texto reconhecido")
    p.add_argument(
        "--exportar_texto", "--exportar-texto",
        action="store_true",
        help="criar arquivos .txt e .json, com o texto separado por página",
    )
    p.set_defaults(qualidade_alta=True)
    return p


def verificar_instalacao() -> None:
    try:
        import ocrmypdf  # noqa: F401
    except ImportError as exc:
        raise RuntimeError("OCRmyPDF não está instalado. Execute o instalador deste projeto.") from exc

    executavel = shutil.which("tesseract")
    if not executavel:
        raise RuntimeError("Tesseract não foi encontrado. Execute o instalador deste projeto.")


def destino_padrao(entrada: Path) -> Path:
    return entrada.with_name(f"{entrada.stem}_ocr.pdf")


def arquivos_da_pasta() -> list[Path]:
    """Retorna os PDFs ainda não convertidos da pasta padrão `arquivos`."""
    pasta = Path(__file__).resolve().parent / "arquivos"
    pasta.mkdir(exist_ok=True)
    pendentes: list[Path] = []
    for arquivo in pasta.iterdir():
        if not arquivo.is_file() or arquivo.suffix.lower() != ".pdf":
            continue
        if arquivo.stem.lower().endswith("_ocr"):
            continue
        resultado = destino_padrao(arquivo)
        if not resultado.exists() or arquivo.stat().st_mtime > resultado.stat().st_mtime:
            pendentes.append(arquivo)
    return sorted(pendentes)


def exportar_texto(saida: Path, criar_json: bool) -> None:
    """Extrai a camada textual final, incluindo páginas que já tinham texto."""
    try:
        from pdfminer.high_level import extract_text
    except ImportError as exc:
        raise RuntimeError("Não foi possível carregar o extrator de texto PDF.") from exc

    conteudo = extract_text(str(saida))
    arquivo_txt = saida.with_suffix(".txt")
    arquivo_txt.write_text(conteudo, encoding="utf-8")
    print(f"Texto criado: {arquivo_txt.resolve()}")

    if criar_json:
        # O pdfminer separa as páginas com o caractere form feed (\f).
        paginas = conteudo.split("\f")
        if paginas and not paginas[-1].strip():
            paginas.pop()
        dados = {
            "arquivo_pdf": saida.name,
            "total_paginas": len(paginas),
            "idioma": "português",
            "paginas": [
                {"pagina": numero, "texto": texto.strip()}
                for numero, texto in enumerate(paginas, 1)
            ],
        }
        arquivo_json = saida.with_suffix(".json")
        arquivo_json.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"JSON criado: {arquivo_json.resolve()}")


def converter(
    entrada: Path,
    saida: Path,
    idiomas: str,
    forcar: bool,
    texto: bool,
    criar_json: bool,
    qualidade_alta: bool,
) -> None:
    if not entrada.is_file() or entrada.suffix.lower() != ".pdf":
        raise ValueError(f"Não é um PDF válido: {entrada}")
    if entrada.resolve() == saida.resolve():
        raise ValueError("A entrada e a saída não podem ser o mesmo arquivo.")
    saida.parent.mkdir(parents=True, exist_ok=True)

    comando = [
        sys.executable, "-m", "ocrmypdf",
        "--language", idiomas,
        "--rotate-pages",
        "--deskew",
        "--output-type", "pdf",
        "--optimize", "1",
    ]
    ambiente = os.environ.copy()
    nome_modelo = ".tessdata_best" if qualidade_alta else ".tessdata_fast"
    tessdata = Path(__file__).resolve().parent / nome_modelo
    if not (tessdata / "por.traineddata").is_file() or not (tessdata / ".installed").is_file():
        raise RuntimeError("O modelo de português não está instalado. Execute novamente o instalador.")
    ambiente["TESSDATA_PREFIX"] = str(tessdata)
    if qualidade_alta:
        comando.extend([
            "--oversample", "400",
            "--tesseract-oem", "1",
            "--tesseract-pagesegmode", "3",
        ])
    comando.append("--force-ocr" if forcar else "--skip-text")
    # Gera primeiro em um temporário: um resultado anterior só é substituído
    # depois que a conversão nova termina corretamente.
    with tempfile.NamedTemporaryFile(
        prefix=f".{saida.stem}_", suffix=".pdf", dir=saida.parent, delete=False
    ) as temporario:
        saida_temporaria = Path(temporario.name)
    saida_temporaria.unlink()
    try:
        comando.extend([str(entrada), str(saida_temporaria)])
        subprocess.run(comando, check=True, env=ambiente)
        saida_temporaria.replace(saida)
    finally:
        saida_temporaria.unlink(missing_ok=True)
    if texto or criar_json:
        exportar_texto(saida, criar_json)


def main() -> int:
    args = parser().parse_args()
    entradas = args.arquivos or arquivos_da_pasta()
    if not entradas:
        print("Nenhum PDF pendente foi encontrado na pasta 'arquivos'.")
        print("Coloque os PDFs nessa pasta ou informe os nomes no comando.")
        return 1
    idiomas = "por"
    try:
        verificar_instalacao()
        for numero, entrada in enumerate(entradas, 1):
            saida = destino_padrao(entrada)
            print(f"\n[{numero}/{len(entradas)}] {entrada.name} -> {saida.name}")
            converter(
                entrada, saida, idiomas, args.forcar,
                args.texto or args.exportar_texto,
                args.exportar_texto,
                args.qualidade_alta,
            )
            print(f"Concluído: {saida.resolve()}")
    except (RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"\nErro: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
