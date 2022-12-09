## info
dist has windows exe soft (https://github.com/krol44/control-stand-mic-led/raw/master/soft-stand-mic-led/dist/stand-mic-led.exe), listening default microphone and send request to esp

## create exe
python -m PyInstaller --onefile .\stand-mic-led.py --windowed

## windows 10 Startup Folder
C:\Users\[User Name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
