#!/usr/bin/env python3
"""Interface gráfica do AcervoOCR para Windows."""

from __future__ import annotations

import os
import sys
from pathlib import Path

from PySide6.QtCore import QObject, Qt, QThread, QTimer, Signal
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pdf_ocr import arquivos_da_pasta, converter, destino_padrao, verificar_instalacao


def configurar_ambiente_empacotado() -> None:
    """Faz o OCRmyPDF localizar o Tesseract incluído no aplicativo."""
    if not getattr(sys, "frozen", False):
        return
    pasta_aplicativo = Path(sys.executable).resolve().parent
    pasta_tesseract = pasta_aplicativo / "tesseract"
    if pasta_tesseract.is_dir():
        os.environ["PATH"] = str(pasta_tesseract) + os.pathsep + os.environ.get("PATH", "")


class AreaSoltar(QLabel):
    arquivos_recebidos = Signal(list)

    def __init__(self) -> None:
        super().__init__("Arraste seus arquivos PDF para esta área\n\nou clique em “Selecionar PDFs”")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAcceptDrops(True)
        self.setMinimumHeight(150)
        self.setObjectName("areaSoltar")

    def dragEnterEvent(self, evento: QDragEnterEvent) -> None:
        if any(url.toLocalFile().lower().endswith(".pdf") for url in evento.mimeData().urls()):
            evento.acceptProposedAction()

    def dropEvent(self, evento: QDropEvent) -> None:
        arquivos = [
            url.toLocalFile()
            for url in evento.mimeData().urls()
            if url.isLocalFile() and url.toLocalFile().lower().endswith(".pdf")
        ]
        if arquivos:
            self.arquivos_recebidos.emit(arquivos)
            evento.acceptProposedAction()


class Conversor(QObject):
    progresso = Signal(int, int, str)
    concluido = Signal(list)
    falhou = Signal(str)

    def __init__(self, arquivos: list[Path], alta: bool, txt: bool, json_: bool) -> None:
        super().__init__()
        self.arquivos = arquivos
        self.alta = alta
        self.txt = txt
        self.json = json_

    def executar(self) -> None:
        resultados: list[str] = []
        try:
            verificar_instalacao()
            total = len(self.arquivos)
            for indice, entrada in enumerate(self.arquivos, 1):
                saida = destino_padrao(entrada)
                self.progresso.emit(indice, total, entrada.name)
                converter(
                    entrada,
                    saida,
                    "por",
                    False,
                    self.txt or self.json,
                    self.json,
                    self.alta,
                )
                resultados.append(str(saida.resolve()))
            self.concluido.emit(resultados)
        except Exception as erro:  # Exibido de forma compreensível na interface.
            self.falhou.emit(str(erro))


class Janela(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AcervoOCR — PDF pesquisável em português")
        self.resize(760, 650)
        self.thread: QThread | None = None
        self.worker: Conversor | None = None

        titulo = QLabel("AcervoOCR")
        titulo.setObjectName("titulo")
        subtitulo = QLabel(
            "Transforme documentos digitalizados em PDFs pesquisáveis,\n"
            "preservando a aparência das páginas."
        )
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.area = AreaSoltar()
        self.area.arquivos_recebidos.connect(self.adicionar_arquivos)
        self.lista = QListWidget()
        self.lista.setMinimumHeight(130)

        selecionar = QPushButton("Selecionar PDFs")
        selecionar.clicked.connect(self.selecionar)
        remover = QPushButton("Remover selecionado")
        remover.clicked.connect(self.remover)
        limpar = QPushButton("Limpar lista")
        limpar.clicked.connect(self.lista.clear)

        botoes_lista = QHBoxLayout()
        botoes_lista.addWidget(selecionar)
        botoes_lista.addWidget(remover)
        botoes_lista.addWidget(limpar)

        self.alta = QCheckBox("Alta qualidade (mais preciso, porém mais lento)")
        self.alta.setChecked(True)
        self.txt = QCheckBox("Criar também arquivo de texto (.txt)")
        self.json = QCheckBox("Criar também arquivo estruturado (.json)")

        self.converter_botao = QPushButton("Converter arquivos")
        self.converter_botao.setObjectName("converter")
        self.converter_botao.clicked.connect(self.iniciar)
        self.barra = QProgressBar()
        self.barra.setValue(0)
        self.estado = QLabel("Adicione um ou mais arquivos PDF para começar.")
        self.estado.setWordWrap(True)

        conteudo = QVBoxLayout()
        conteudo.setContentsMargins(32, 25, 32, 25)
        conteudo.setSpacing(14)
        conteudo.addWidget(titulo, alignment=Qt.AlignmentFlag.AlignCenter)
        conteudo.addWidget(subtitulo)
        conteudo.addWidget(self.area)
        conteudo.addLayout(botoes_lista)
        conteudo.addWidget(self.lista)
        conteudo.addWidget(self.alta)
        conteudo.addWidget(self.txt)
        conteudo.addWidget(self.json)
        conteudo.addWidget(self.converter_botao)
        conteudo.addWidget(self.barra)
        conteudo.addWidget(self.estado)

        central = QWidget()
        central.setLayout(conteudo)
        self.setCentralWidget(central)
        self.setStyleSheet("""
            QMainWindow { background: #f5f2eb; }
            QLabel#titulo { color: #283b36; font-size: 30px; font-weight: 700; }
            QLabel#areaSoltar { border: 2px dashed #58766d; border-radius: 12px;
                background: #ffffff; color: #344b44; font-size: 16px; }
            QPushButton { padding: 9px 15px; border: 1px solid #829b93;
                border-radius: 6px; background: #ffffff; }
            QPushButton:hover { background: #e8efec; }
            QPushButton#converter { color: white; background: #365f52;
                font-size: 16px; font-weight: 600; padding: 12px; }
            QPushButton#converter:hover { background: #294c41; }
            QPushButton:disabled { background: #aebbb7; }
            QListWidget { background: white; border: 1px solid #c7d0cc; border-radius: 6px; }
        """)
        automaticos = [str(p) for p in arquivos_da_pasta()]
        self.adicionar_arquivos(automaticos)
        if automaticos:
            self.estado.setText("PDFs encontrados na pasta “arquivos”. A conversão começará automaticamente.")
            QTimer.singleShot(500, self.iniciar)

    def selecionar(self) -> None:
        arquivos, _ = QFileDialog.getOpenFileNames(self, "Selecione os PDFs", "", "PDF (*.pdf)")
        self.adicionar_arquivos(arquivos)

    def adicionar_arquivos(self, arquivos: list[str]) -> None:
        existentes = {self.lista.item(i).text() for i in range(self.lista.count())}
        for nome in arquivos:
            caminho = str(Path(nome).resolve())
            if caminho not in existentes:
                self.lista.addItem(caminho)
                existentes.add(caminho)
        self.estado.setText(f"{self.lista.count()} arquivo(s) na lista.")

    def remover(self) -> None:
        for item in self.lista.selectedItems():
            self.lista.takeItem(self.lista.row(item))
        self.estado.setText(f"{self.lista.count()} arquivo(s) na lista.")

    def iniciar(self) -> None:
        arquivos = [Path(self.lista.item(i).text()) for i in range(self.lista.count())]
        if not arquivos:
            QMessageBox.information(self, "Nenhum arquivo", "Adicione pelo menos um arquivo PDF.")
            return
        self.converter_botao.setEnabled(False)
        self.barra.setRange(0, 0)
        self.estado.setText("Preparando o reconhecimento de texto...")

        self.thread = QThread(self)
        self.worker = Conversor(arquivos, self.alta.isChecked(), self.txt.isChecked(), self.json.isChecked())
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.executar)
        self.worker.progresso.connect(self.atualizar)
        self.worker.concluido.connect(self.finalizar)
        self.worker.falhou.connect(self.erro)
        self.worker.concluido.connect(self.thread.quit)
        self.worker.falhou.connect(self.thread.quit)
        self.thread.start()

    def atualizar(self, atual: int, total: int, nome: str) -> None:
        self.estado.setText(f"Processando {atual} de {total}: {nome}\nNão feche o programa.")

    def restaurar(self) -> None:
        self.barra.setRange(0, 100)
        self.barra.setValue(100)
        self.converter_botao.setEnabled(True)

    def finalizar(self, resultados: list[str]) -> None:
        self.restaurar()
        self.estado.setText("Conversão concluída.")
        QMessageBox.information(
            self,
            "Conversão concluída",
            "Os arquivos pesquisáveis foram criados ao lado dos originais:\n\n" + "\n".join(resultados),
        )

    def erro(self, mensagem: str) -> None:
        self.restaurar()
        self.estado.setText("A conversão não foi concluída.")
        QMessageBox.critical(self, "Não foi possível converter", mensagem)


def main() -> int:
    configurar_ambiente_empacotado()
    app = QApplication(sys.argv)
    app.setApplicationName("AcervoOCR")
    janela = Janela()
    janela.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
