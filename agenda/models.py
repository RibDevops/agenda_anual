from django.db import models


class TipoEvento(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    tipo_id = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    data = models.DateField()
    cor = models.CharField(max_length=20)  # ex: red, blue, yellow

    def __str__(self):
        return f"{self.titulo} - {self.data}"
