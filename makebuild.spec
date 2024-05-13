# -*- mode: python ; coding: utf-8 -*-
#
# Copy/Paste below into command prompt
# C:\Users\[path]\PycharmProjects\[project]\venv\Scripts\pyinstaller.exe C:\Users\[path]\PycharmProjects\[project]\build.spec

block_cipher = None

import PyInstaller.config
from pathlib import Path

workfolder = str(Path().absolute())

PyInstaller.config.CONF['distpath'] = f"{workfolder}"

a = Analysis(['build.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='makebuild',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
