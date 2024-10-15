from rest_framework import viewsets
from .models import login,Event,log
from  .serializer import EventSerializer,LoginSerializer,logSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset=login.objects.all()
    serializer_class=LoginSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

class logViewSet(viewsets.ModelViewSet):
    queryset=log.objects.all()
    serializer_class=logSerializer