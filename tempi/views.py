from django.http import HttpResponse
from django.shortcuts import render

from pprint import pprint as pp

from tempi.models import Tempo


def index(request):
    return HttpResponse("ciaooo")


def gare(request):
    gare_mattino = Tempo.objects.all().filter(turno='M')
    gare_pomeriggio = Tempo.objects.all().filter(turno='P')

    context = {'gare_mattino': gare_mattino,
               'gare_pomeriggio': gare_pomeriggio,
               }

    return render(request, 'tempi/gare.html', context)
