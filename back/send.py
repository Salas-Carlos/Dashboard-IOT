import json
import requests

import websocket
import random,time
from websocket import create_connection

ws = create_connection('ws://localhost:8000/ws/some_url/')
for i in range(1000):
    time.sleep(3)
    ws.send(json.dumps({'Temperatura':random.randint(20,60), "Humedad":random.randint(20,60) }))
ws.close()