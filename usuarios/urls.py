from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('valida_login/', views.valida_login, name = 'valida_login'),
    path('disciplina/', views.disciplina, name = 'disciplina'),
    path('caddisciplina/', views.caddisciplina, name = 'caddisciplina'),
    path('ac/', views.ac, name = 'ac'),
    path('al/', views.al, name = 'al'),
    path('md/', views.md, name = 'md'),
    path('mc/', views.mc, name = 'mc'),

]
