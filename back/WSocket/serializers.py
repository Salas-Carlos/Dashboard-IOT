from rest_framework import serializers
from .models import AmbientalDates


class AmbientalDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbientalDates
        fields = '__all__'