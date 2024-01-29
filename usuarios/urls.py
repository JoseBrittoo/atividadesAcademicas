from django.urls import path 
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('valida_login/', views.valida_login, name = 'valida_login'),
    path('acessar_disciplina/<int:disciplina_id>/', views.acessar_disciplina, name='acessar_disciplina'),
    path('paginaInicial/', views.paginaInicial, name = 'paginaInicial'),
    path('menu/', views.menu, name = 'menu'),
    path('gradeCurricular/', views.gradeCurricular, name = 'gradeCurricular'),
    path('nova_tarefa/', views.nova_tarefa, name = 'nova_tarefa'),
    path('calendario/', views.calendario, name = 'calendario'),
    path('lista_eventos/', views.lista_eventos, name = 'lista_eventos'),
    path('criar_evento/', views.criar_evento, name = 'criar_evento'),
    path('atualizar_evento/<evento_id>/', views.atualizar_evento, name = 'atualizar_evento'),
    path('deletar_evento/<evento_id>/', views.deletar_evento, name = 'deletar_evento'),
    path('lista_disciplina/', views.lista_disciplina, name = 'lista_disciplina'),
    path('cadastro_disciplina/', views.cadastro_disciplina, name = 'cadastro_disciplina'),
    path('atualizar_disciplina/<disciplina_id>/', views.atualizar_disciplina, name = 'atualizar_disciplina'),
    path('deletar_disciplina/<disciplina_id>/', views.deletar_disciplina, name = 'deletar_disciplina'),
    path('grade_curricular/', views.gradeCurricular, name='grade_curricular'),
    path('adicionar_periodo/', views.adicionarPeriodo, name='adicionar_periodo'),
    path('adicionar_disciplina/', views.adicionarDisciplina, name='adicionar_disciplina')
]
