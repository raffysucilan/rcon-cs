# RCON_CS
A simple CLI created in Python to run RCON commands for Counter-Strike 1.6 dedicated servers.

## Compile from Source (Windows)
1. Install Python - https://www.python.org/downloads
2. Install Git - https://git-scm.com/install/windows
3. Open Command Prompt.
4. Install Pyinstaller - `pip install pyinstaller`
5. Clone repo - `git clone https://github.com/raffysucilan/rcon-cs.git`
6. Compile source - `pyinstaller --onefile rcon_cs.py`

Compiled binary will be in "dist" folder.

## How to Use
### Sample Batch File
```
@echo off

set IP=0.0.0.0 
set PORT=0
set PASSWORD=

rem Using Binary
rcon_cs -i %IP% -p %PORT% -a %PASSWORD% status

rem Using Script
python rcon_cs.py -i %IP% -p %PORT% -a %PASSWORD% status

pause
```