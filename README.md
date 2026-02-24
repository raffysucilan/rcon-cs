# RCON_CS
A simple CLI created in Python to run RCON commands for Counter-Strike 1.6 dedicated servers.

## How to Use
Download the [latest release](https://github.com/raffysucilan/rcon-cs/releases).
### Sample Standalone.bat
```
@echo off

set IP=0.0.0.0 
set PORT=0
set PASSWORD=

rcon_cs -i %IP% -p %PORT% -a %PASSWORD% status

pause
```
### Sample Interactive.bat
Interactive mode allows the connection to be open as long as the window is alive.  
When the connection is open, only commands are required by the CLI.
```
@echo off

set IP=0.0.0.0 
set PORT=0
set PASSWORD=

rcon_cs -i %IP% -p %PORT% -a %PASSWORD%
```
## Compile from Source (Windows)
### Using [PYInstaller](https://pypi.org/project/pyinstaller)
`pyinstaller --onefile rcon_cs.py`