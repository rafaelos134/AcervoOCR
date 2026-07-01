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
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("arquivos", nargs="*", type=Path, help="PDFs de entrada")
    p.add_argument("--forcar", action="store_true", help="refazer OCR inclusive em páginas que já têm texto")
    p.add_argument("--somente-portugues", action="store_true", help=argparse.SUPPRESS)
    p.add_argument(
        "--qualidade_alta",
        action="store_true",
        help="usa tessdata_best, somente português e processamento em 400 DPI (mais lento)",
    )
    p.add_argument("--texto", action="store_true", help="criar também um arquivo .txt com o texto reconhecido")
    p.add_argument(
        "--exportar_texto", "--exportar-texto",
        action="store_true",
        help="criar arquivos .txt e .json, com o texto separado por página",
    )
    return p


def selecionar_pdfs() -> list[Path]:
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError:
        return []
    root = tk.Tk()
    root.withdraw()
    nomes = filedialog.askopenfilenames(
        title="Selecione os PDFs para aplicar OCR",
        filetypes=[("Arquivos PDF", "*.pdf")],
    )
    root.destroy()
    return [Path(nome) for nome in nomes]


def perguntar_alta_qualidade() -> bool:
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.withdraw()
    resposta = messagebox.askyesno(
        "Qualidade do reconhecimento",
        "Deseja usar o modo de alta qualidade?\n\n"
        "Ele é recomendado para páginas antigas, letras pequenas ou imagens desgastadas, "
        "mas demora mais.\n\nEscolha “Não” para o modo normal e mais rápido.",
        parent=root,
    )
    root.destroy()
    return resposta


def mostrar_mensagem(titulo: str, mensagem: str, erro: bool = False) -> None:
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        (messagebox.showerror if erro else messagebox.showinfo)(titulo, mensagem)
        root.destroy()
    except Exception:
        pass


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
    modo_grafico = not args.arquivos
    entradas = args.arquivos or selecionar_pdfs()
    if not entradas:
        print("Nenhum PDF selecionado.")
        return 1
    if modo_grafico:
        args.qualidade_alta = perguntar_alta_qualidade()
    idiomas = "por"
    concluidos: list[Path] = []
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
            concluidos.append(saida.resolve())
    except (RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"\nErro: {exc}", file=sys.stderr)
        if modo_grafico:
            mostrar_mensagem("Não foi possível concluir", str(exc), erro=True)
        return 1
    if modo_grafico:
        mostrar_mensagem(
            "OCR concluído",
            "Os documentos pesquisáveis foram criados:\n\n" + "\n".join(map(str, concluidos)),
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
