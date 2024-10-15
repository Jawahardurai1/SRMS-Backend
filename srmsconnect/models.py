from django.db import models
class login(models.Model):
    name=models.CharField(max_length=20)
    roll=models.CharField(max_length=20)
    cls=models.CharField(max_length=20)
    plc=models.CharField(max_length=20)
    dplc=models.CharField(max_length=20)
    prb=models.TextField(max_length=100)
    # img=models.ImageField(max_length=20)

class Event(models.Model):
    eve=models.CharField(max_length=20)
    venue=models.CharField(max_length=20)
    DT=models.DateTimeField()
    contact=models.IntegerField(max_length=10)
    poster=models.ImageField(upload_to='img/',max_length=300)

class log(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
