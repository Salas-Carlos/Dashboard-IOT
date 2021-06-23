from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .consumers import WSConsumer
from .serializers import AmbientalDatesSerializer
from .models import AmbientalDates
from websocket import create_connection
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.



@api_view(['POST'])
def index(request):
        Humedad = request.data.get("Humedad")
        Temperatura = request.data.get("Temperatura")

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
        "dashboard",  
        {
            "type": "deprocessing",   
            "Temperatura": Temperatura,
            "Humedad": Humedad
        },
    )  

        return Response({"Nice": "1"})

 
