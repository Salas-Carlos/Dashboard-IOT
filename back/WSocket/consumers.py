import json
from random import randint
from time import sleep
from .models import AmbientalDates
from io import open
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import sync_to_async
import os


class WSConsumer(AsyncWebsocketConsumer):
   
    
    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()
       
    async def disconnect(self,close_code):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        Temperatura =datapoint['Temperatura']
        Humedad = datapoint["Humedad"]
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'Temperatura': Temperatura,
                'Humedad': Humedad
            }
        )

      

    async def deprocessing(self,event):
        Temperatura=event['Temperatura']
        Humedad=event['Humedad']
        await self.send(text_data=json.dumps({'Temperatura':Temperatura, 'Humedad': Humedad}))
 

       
    def lectura(self):
        file = open("texto.txt","r")
        lectura = file.read()
        file.close()
        return lectura

    def escritura(self, body):
        file = open("texto.txt","w")
        lectura = file.write(body)
        file.close()



"""
self.accept()
        dato = AmbientalDates.objects.get(id = 1)         
        ob = {"Temperatura": dato.Temperatura, "Humedad": dato.Humedad }
        if str(ob) != self.lectura(): 
            self.send(text_data=json.dumps(ob))
            self.escritura(str(ob))
                #self.send(text_data=json.dumps(dato))
        else:
            self.send(text_data=json.dumps({"Temperatura": "null", "Humedad": "null"}))
"""