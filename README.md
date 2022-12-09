Pantograph Alctron MA616XL has the LED, and set of scripts will be allowing to control it
===
How is it working?
* In the windows is listening default microphone and the sound level check on volume after sending state on or off to the esp8266 v3
Next, esp is clicking on the button on the pantograph :yum:

Why do I need this?
* Pantographs with LED are very expensive ($1000+) with control

## Demo
![Pantograph Alctron MA616XL demo](https://github.com/krol44/control-stand-mic-led/blob/master/content/demo.gif?raw=true)

## important
**this is not full manual :sweat_smile: if you need more information - create issue**

## Soldering
will add if you need

## setup windows
edit hosts (example):
#ip of esp
192.168.1.44    esp-stand-mic.krol44.com

run exe, more information is here https://github.com/krol44/control-stand-mic-led/tree/master/soft-stand-mic-led#readme

## setup esp
`pip install esptool`
`pip install adafruit-ampy `https://github.com/scientifichackers/ampy`

### Flash MicroPython
/dev/tty.usbserial-0001 - device esp
```
esptool.py --port /dev/tty.usbserial-0001 erase_flash
esptool.py --port /dev/tty.usbserial-0001 --baud 115200 write_flash --flash_size=detect 0 esp-stand-mic-led/esp8266-20220618-v1.19.1.bin
```

### check
`ampy -p /dev/tty.usbserial-0001 -b 96000 ls`

### edit esp-stand-mic-led/main.py
setup var:
* pinOut = 5
* serverIp = '0.0.0.0'
* serverPort = 8074
* wifiSsid = ''
* wifiPass = ''

### put main.py to the esp
`ampy -p /dev/tty.usbserial-0001 -b 96000 put esp-stand-mic-led/main.py`

## settings (not necessary)
`export AMPY_PORT=/dev/tty.usbserial-0001`

## info
```
Commands ampy:
  get    Retrieve a file from the board.
  ls     List contents of a directory on the board.
  mkdir  Create a directory on the board.
  put    Put a file or folder and its contents on the board.
  reset  Perform soft reset/reboot of the board.
  rm     Remove a file from the board.
  rmdir  Forcefully remove a folder and all its children from the board.
  run    Run a script and print its output.
```
