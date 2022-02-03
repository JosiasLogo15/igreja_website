from pyexpat import model
from statistics import mode
from django.db import models

class Eventos(models.Model):
    culto = [
        ('TR', 'Terça-Feira'),
        ('QT', 'Quinta-Feira'),
        ('SB', 'Sábado'),
        ('DM', 'Domingo'),
    ]
    cultos = models.CharField(max_length=200, choices=culto, blank=False, null=False)
    eventos = models.CharField(max_length=200, blank=False, null=False)
    