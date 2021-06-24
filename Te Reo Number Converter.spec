# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['build_files/TeReoNumberConverter_GUI.py'],
             pathex=['/Users/jacob/Desktop/TeReoNumberConverter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Te Reo Number Converter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='build_files/Icon.ico')
app = BUNDLE(exe,
             name='Te Reo Number Converter.app',
             icon='./build_files/Icon.ico',
             bundle_identifier=None)
