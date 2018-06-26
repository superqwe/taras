from django.db import models

MF = (
    ('M', 'Maschile'),
    ('F', 'Femminile'),
)

TURNO = (
    ('M', 'Mattina'),
    ('P', 'Pomeriggio')
)


# Create your models here.

class Squadra(models.Model):
    nome = models.CharField(max_length=200)
    mf = models.CharField('Maschile/Femminile', max_length=1,
                          choices=MF,
                          default='M'
                          )

    class Meta:
        ordering = ['nome', '-mf']
        verbose_name_plural = 'Squadre'

    def __str__(self):
        return '%s %s' % (self.mf, self.nome)


class Barca(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Barche'

    def __str__(self):
        return self.nome


class Tempo(models.Model):
    n = models.IntegerField(default=1)
    turno = models.CharField(max_length=1,
                             choices=TURNO,
                             default='M'
                             )
    squadra = models.ForeignKey(Squadra, on_delete=models.CASCADE)
    barca = models.ForeignKey(Barca, null=True, blank=True, on_delete=models.CASCADE)
    tempo = models.DurationField(null=True, blank=True)

    class Meta:
        ordering = ['n', 'turno']
        verbose_name_plural = 'Tempi'

    def __str__(self):
        return '%i - %s - %s %s - %s' % (self.n, self.squadra, self.tempo, self.turno, self.barca,)
