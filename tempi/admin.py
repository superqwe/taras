from django.contrib import admin

from .models import Tempo, Squadra, Barca

class TempoAdmin(admin.ModelAdmin):
    list_display = ('n', 'turno', 'squadra', 'barca', 'tempo')

# Register your models here.
admin.site.register(Tempo, TempoAdmin)
admin.site.register(Barca)
admin.site.register(Squadra)
