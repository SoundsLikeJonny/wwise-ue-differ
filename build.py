import subprocess
from datetime import datetime
from pathlib import Path

command = str(Path.joinpath(Path().absolute(), '.venv/Scripts/pyinstaller.exe'))
windowed = '--w'
args = str(Path.joinpath(Path().absolute(), 'build.spec'))

current_date_time = '\n\n\nNEW BUILD STARTED\n=========\n' + str(datetime.now().strftime("%d %B, %Y %H:%M,%S")) + '\n\n\n'

err = open('build_log.txt', 'a')
err.write(current_date_time)
err.flush()

print([command, windowed, args])

c = subprocess.Popen([command, args], stderr=err, shell=True, close_fds=True, universal_newlines=True)
print(str(c))
c.wait()
