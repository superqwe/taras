from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from tempi.models import Tempo


def index(request):
    return HttpResponse("ciaooo")


def gare(request):
    gare = Tempo.objects.all()
    context = {'gare': gare}
    return render(request, 'tempi/gare.html', context)
