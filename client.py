import networkx
import timefrom 
import machine import Pin, ADC
import usocket as socket
import ustruct as struct

SSID = "TU_WIFI"
PASSWORD = "TU_PASSWORD"
SERVER_IP = "192.168.20.142" 
SERVER_PORT = 8765

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Conecting to WiFi...")
        time.sleep(1)
    print("Connectado:", wlan.ifconfig())

led=Pin (2, Pin.OUT)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)






from uwebsockets.client import connect

connect_wifi()

try:
    with connect (f"ws://{SERVER_IP}:{SERVER_PORT}") as ws:
        print("Conectado al servidor NiceGUI")
        while True:
            val = pot.read()
            ws.send(str(val))
            try:
                msg = ws.recv()
                if msg == "ON":
                    led.values(1)
                elif msg == "OFF":
                    led.value(0)
            except:
                pass
            time.sleep(0.1)
except Exception as e:
    print("Error:", e)