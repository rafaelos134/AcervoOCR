# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

ocr_datas, ocr_binaries, ocr_hidden = collect_all("ocrmypdf")
pdf_datas, pdf_binaries, pdf_hidden = collect_all("pdfminer")

datas = ocr_datas + pdf_datas + [
    (".tessdata_fast", ".tessdata_fast"),
    (".tessdata_best", ".tessdata_best"),
]
binaries = ocr_binaries + pdf_binaries
hiddenimports = ocr_hidden + pdf_hidden

a = Analysis(
    ["acervo_ocr_gui.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter"],
    noarchive=False,
    optimize=1,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="AcervoOCR",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="AcervoOCR",
)
