from django.contrib import admin

from .models import Tempo, Squadra, Barca

# Register your models here.
admin.site.register(Tempo)
admin.site.register(Barca)
admin.site.register(Squadra)
