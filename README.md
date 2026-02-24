# RCON_CS
A simple CLI created in Python to run RCON commands for Counter-Strike 1.6 dedicated servers.

## How to Use
Download the [latest release](https://github.com/raffysucilan/rcon-cs/releases).
### Standalone Mode
This is a sample command to get the server status.  
`rcon_cs -i IP -p PORT -a PASSWORD status`
### Interactive Mode
Interactive mode allows the connection to stay open as long as the window is alive.  
When the connection is open, only the actual commands are required by the CLI.

This is a sample .bat that will open a persistent window.
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