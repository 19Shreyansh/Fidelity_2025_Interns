from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class TripDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trip
        fields=['boardingpoint', 'destination', 'trip_cost']