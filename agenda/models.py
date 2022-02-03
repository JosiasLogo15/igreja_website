from django.db import models
from eventos.models import Eventos
class Agenda(models.Model):
    calendario = models.DateField(blank=False, null=False, auto_now=False, auto_now_add=False)
    evento = models.ForeignKey("eventos.Eventos", on_delete=models.CASCADE)