from rest_framework import serializers
from .models import login,Event,log
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields=('id','name','roll','cls','plc','dplc','prb')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','eve', 'venue', 'DT', 'contact','poster')

class logSerializer(serializers.ModelSerializer):
    class Meta:
        model = log
        fields = ('id','username','password')