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
    
#Isso é relacionado a grade curricular
class DisciplinaG(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Periodo(models.Model):
    numero = models.IntegerField()
    disciplinas = models.ManyToManyField(DisciplinaG)

    def __str__(self):
        return f'Período {self.numero}'
    
class GradeCurricular(models.Model):
    nome_curso = models.CharField(max_length=100)
    duracao_curso = models.IntegerField()
    descricao_curso = models.TextField()

    periodos = models.ManyToManyField(Periodo)

    def __str__(self):
        # Retorne uma representação da grade curricular, como o nome do curso
        # Por exemplo:
        # return self.nome_curso if self.nome_curso else "Grade Curricular"
        return "Grade Curricular"
    
class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length = 100)
    descricao_disciplina = models.TextField(blank = True)

    def __str__(self) -> str:
        return self.nome_disciplina
