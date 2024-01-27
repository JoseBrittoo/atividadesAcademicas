from django import forms
from django.forms import ModelForm
from .models import Evento, Disciplina

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data_evento', 'hora_evento', 'descricao']
        labels = {
            'nome':'Nome do evento',
            'data_evento': 'Data do evento',
            'hora_evento': 'Hora do evento',
            'descricao': 'Descrição'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'data_evento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_evento': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome_disciplina', 'descricao_disciplina']
        labels = {
            'nome_disciplina': '',
            'descricao_disciplina': 'Descrição'
        }
        widgets = {
            'nome_disciplina': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Disciplina'}),
            'descricao_disciplina': forms.TextInput(attrs={'class': 'input descricao-input', 'placeholder': '', 'style': 'margin-left: 10%; margin-right: 10%; padding: 4%'}),
        }