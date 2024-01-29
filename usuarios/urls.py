from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('valida_login/', views.valida_login, name = 'valida_login'),
    path('disciplina/', views.disciplina, name = 'disciplina'),
    path('caddisciplina/', views.caddisciplina, name = 'caddisciplina'),
    #Adicionado para ir direto para anexar arquivo
    path('caddisciplina/anexar-arquivo/<int:disciplina_id>/', views.anexar_arquivo, name='anexar_arquivo'),
    path('ac/', views.ac, name = 'ac'),
    path('al/', views.al, name = 'al'),
    path('md/', views.md, name = 'md'),
    path('mc/', views.mc, name = 'mc'),
    path('paginaInicial/', views.paginaInicial, name = 'paginaInicial'),
    path('menu/', views.menu, name = 'menu'),
    path('gradeCurricular/', views.gradeCurricular, name = 'gradeCurricular'),
    path('novatarefa/', views.novatarefa, name = 'novatarefa'),
    path('calendario/', views.calendario, name = 'calendario'),
    path('lista_eventos/', views.lista_eventos, name = 'lista_eventos'),
    path('criar_evento/', views.criar_evento, name = 'criar_evento'),
    path('atualizar_evento/<evento_id>', views.atualizar_evento, name = 'atualizar_evento'),
    path('deletar_evento/<evento_id>', views.deletar_evento, name = 'deletar_evento'),
    path('lista_disciplina', views.lista_disciplina, name = 'lista_disciplina'),
    path('cadastro_disciplina', views.cadastro_disciplina, name = 'cadastro_disciplina'),
    path('atualizar_disciplina/<disciplina_id>', views.atualizar_disciplina, name = 'atualizar_disciplina'),
    path('deletar_disciplina/<disciplina_id>', views.deletar_disciplina, name = 'deletar_disciplina'),
    #path('grade_curricular/', views.gradeCurricular, name='grade_curricular'),
    path('adicionar_periodo/', views.adicionarPeriodo, name='adicionar_periodo'),
    path('adicionar_disciplina/', views.adicionarDisciplina, name='adicionar_disciplina'),
    path('anexar_arquivo/<int:disciplina_id>/', views.anexar_arquivo, name='anexar_arquivo'),
    path('auth/anexar_arquivo/', views.anexar_arquivo, name='anexar_arquivo_default'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)