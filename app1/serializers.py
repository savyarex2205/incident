from rest_framework import serializers
from .models import Users, Incidents

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model= Users
        fields="__all__"

class incidentSerializers(serializers.ModelSerializer):
    class Meta:
        model= Incidents
        fields="__all__"