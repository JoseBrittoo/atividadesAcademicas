from django import forms
from django.forms import ModelForm
from .models import Evento, Disciplina, Periodo, GradeCurricular

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
        fields = ['nome']
        labels = {'nome': 'Nome da Disciplina'}
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})}

class PeriodoForm(ModelForm):
    class Meta:
        model = Periodo
        fields = ['numero', 'disciplinas']
        labels = {'numero': 'Número do Período', 'disciplinas': 'Disciplinas'}
        widgets = {'numero': forms.NumberInput(attrs={'class': 'form-control'}),
                   'disciplinas': forms.CheckboxSelectMultiple}
class GradeCurricularForm(ModelForm):
    class Meta:
        model = GradeCurricular
        fields = ['periodos']
        labels = {'periodos': 'Períodos'}
        widgets = {'periodos': forms.CheckboxSelectMultiple}
        