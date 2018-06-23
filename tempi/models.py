from django.db import models


# Create your models here.

class Squadra(models.Model):
    nome = models.CharField(max_length=200)
    mf = models.CharField(max_length=1)


class Gara(models.Model):
    n = models.IntegerField()
    turno = models.IntegerField()
    squadra1 = models.ForeignKey(Squadra, on_delete=models.CASCADE)
    barca1 = models.CharField(max_length=200)
    tempo1 = models.TimeField()
    squadra2 = models.ForeignKey(Squadra, on_delete=models.CASCADE)
    barca2 = models.CharField(max_length=200)
    tempo2 = models.TimeField()
