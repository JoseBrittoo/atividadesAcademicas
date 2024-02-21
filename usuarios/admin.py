from django.contrib import admin
from .models import Evento, Disciplina, Anexo, Anotacao

admin.site.register(Evento)
admin.site.register(Disciplina)
admin.site.register(Anexo)
admin.site.register(Anotacao)
