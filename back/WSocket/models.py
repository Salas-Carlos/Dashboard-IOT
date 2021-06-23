
from django.db import models

# Create your models here.

   
class AmbientalDates(models.Model):
    Temperatura = models.IntegerField()
    Humedad = models.IntegerField()