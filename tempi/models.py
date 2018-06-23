from django.db import models


# Create your models here.

class Squadra(models.Model):
    nome = models.CharField(max_length=200)
    mf = models.CharField(max_length=1)

class Tempo(models.Model):
    n = models.IntegerField()
    turno = models.IntegerField()
    squadra = models.ForeignKey(Squadra, on_delete=models.CASCADE)
    barca = models.CharField(max_length=200)
    tempo = models.TimeField()
