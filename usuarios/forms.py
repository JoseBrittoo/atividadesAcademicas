from django import forms
from django.forms import ModelForm
from .models import Evento

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