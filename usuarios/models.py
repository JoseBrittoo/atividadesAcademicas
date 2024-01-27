from django.db import models


class Usuario(models.Model):
    email = models.EmailField(max_length = 254)
    senha = models.CharField(max_length = 64)

    def __str__(self) -> str:
        return self.email
    
class Evento(models.Model):
    nome = models.CharField('Nome do evento', max_length = 100)
    data_evento = models.DateTimeField('Data do evento')
    hora_evento = models.TimeField(null=True)
    descricao = models.TextField(blank = True)

    def __str__(self) -> str:
        return self.nome