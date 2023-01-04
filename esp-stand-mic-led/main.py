domainNotifyNewIP = ''
pinRed = 14 #D5
pinBlue = 12 #D6
serverIp = '0.0.0.0'
serverPort = 8074
wifiSsid = ''
wifiPass = ''

from machine import Pin, PWM
import time, ure
import urequests as requests
import network

def do_connect():
    global domain, wifiSsid, wifiPass, serverPort
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifiSsid, wifiPass)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    textMess = 'ip stand mic with led - ' + wlan.ifconfig()[0] + ':' + str(serverPort)
    
    if (domainNotifyNewIP != ''):
        requests.get(domainNotifyNewIP + '/?message=' + textMess)
    
print ('starting...')
do_connect()

led = PWM(Pin(pinRed), 1000)
led.duty(1024)

power = 'off'

def switcher(path):
    print (path)
    global power
    
    if path == '/on' and power == 'on': 
        return power
    
    if path == '/off' and power == 'off': 
        return power
            
    if power == 'off':
        power = 'on'
        for dutyCycle in range(0, 1024):
            led.duty(1024-dutyCycle)
            time.sleep(0.001)
    else:
        power = 'off'
        for dutyCycle in range(0, 1024):
            led.duty(dutyCycle)
            time.sleep(0.001)
        
    return power

def parseURL(url):
    parameters = {}

    path = ure.search('(.*?)(\?|$)', url) 

    while True:
        vars = ure.search('(([a-z0-9]+)=([a-z0-8.]*))&?', url)
        if vars:
            parameters[vars.group(2)] = vars.group(3)
            url = url.replace(vars.group(0), '')
        else:
            break

    return path.group(1), parameters

def buildResponse(response):
    return '''HTTP/1.0 200 OK\r\nContent-type: text/plain\r\nContent-length: %d\r\n\r\n%s''' % (len(response), response)

import socket
addr = socket.getaddrinfo(serverIp, serverPort)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    cl, addr = s.accept()
    #print('client connected from', addr)
    request = str(cl.recv(1024))
    #print('REQUEST: ', request)

    obj = ure.search('GET (.*?) HTTP\/', request)
    #print(obj.group(1))
    
    if not obj:
      cl.send(buildResponse('invalid request'))
    else:
        path, parameters = parseURL(obj.group(1))
        if path == '/on' or path == '/off':
            cl.send(buildResponse(switcher(path)))
        else:
         cl.send(buildResponse('error path, /on or /off'))
        
    cl.close()