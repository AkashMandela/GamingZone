from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    desc=models.TextField( max_length=50)
    date=models.DateField()


class Game(models.Model):
    name=models.CharField(max_length=50)
    image_url=models.CharField(max_length=2083)
    game_type=models.CharField(max_length=50)
    dawnload_link=models.CharField(max_length=2083)
    popularity=models.IntegerField(max_length=1)
    prize=models.FloatField(max_length=10)
