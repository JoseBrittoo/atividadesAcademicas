from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length = 254)
    senha = models.CharField(max_length = 64)

    def __str__(self) -> str:
        return self.email