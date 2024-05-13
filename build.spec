# -*- mode: python ; coding: utf-8 -*-
# "C:\Users\jonev\PycharmProjects\wwise-ue-differ\.venv\Scripts\pyinstaller.exe" --windowed "C:\Users\jonev\PycharmProjects\wwise-ue-differ\build.spec"
# Icons: https://icons8.com/icon/set/folder-link/offices

import PyInstaller.config
from datetime import datetime
import os
from pathlib import Path
from project_info import Info


icon_name = str(Path.joinpath(Path().absolute(), Info.ICON_PATH))

current_date_time = str(datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))


buildnumber = str(datetime.now().strftime("%Y%m%d.%H%M%S"))
buildnumber = f'{Info.PROJECT_TITLE}\n' \
                f'{Info.COMPANY}\n'\
                f'Build: {buildnumber}\n'\
                f'Author: Jon Evans'

try:
        with open('info.txt', 'w') as f:
                for line in buildnumber:
                        f.write(line)
except Exception as e:
        print(str(e))

parent_folder = str(Path.joinpath(Path().absolute(), 'builds', f'{Info.PROJECT_TITLE}_{current_date_time}'))
workfolder = f'{parent_folder}'

os.makedirs(workfolder)
os.startfile(workfolder)

PyInstaller.config.CONF['distpath'] = f"{workfolder}"

block_cipher = None

import glob
analysis_data = []
for path in glob.glob('.\\resources\\*.png'):
        analysis_data.append((path, '.\\resources\\'))

for path in glob.glob('.\\resources\\*.ico'):
        analysis_data.append((path, '.\\resources\\'))

for path in glob.glob('./src/ui/gui/*.ui'):
        analysis_data.append((path, './src/ui/gui/'))

analysis_data = analysis_data + [('./info.txt', './')]
print(analysis_data)

a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=analysis_data,
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
          [],
          exclude_binaries=True,
          name=Info.PROJECT_TITLE,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon=icon_name )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[], name=Info.PROJECT_TITLE)
