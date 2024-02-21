from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from usuarios.models import User, Evento, Disciplina
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Evento, Periodo, Anexo
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import EventoForm, PeriodoForm, DisciplinaGForm, DisciplinaForm, AnexoForm, AnotacaoForm



def home(request):
    return render(request, 'home.html')

def flogin(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def fcadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def acessar_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    return render(request, 'acessar_disciplina.html', {'disciplina': disciplina})

def nova_tarefa(request):
    status = request.GET.get('status')
    return render(request, 'nova_tarefa.html', {'status': status})

def paginaInicial(request):
    return render(request, 'paginaInicial.html')

def menu(request):
    return render(request, 'menu.html')

def valida_cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return redirect('/accounts/fcadastro/?status=1')

        try:
            # Verifica se o nome de usuário já existe
            user = User.objects.get(username=username)
            return redirect('/accounts/fcadastro/?status=2')

        except User.DoesNotExist:
            # Se o usuário não existe, cria o novo usuário
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return redirect('/accounts/flogin/')
    
        
def valida_login(request):
    username = request.POST.get('user')
    password = request.POST.get('password')

    # Autentica o usuário
    user = authenticate(username=username, password=password)

    if user is not None:
        # Verifica se o usuário está ativo
        if user.is_active:
            # Realiza o login
            login(request, user)
            return redirect('/accounts/paginaInicial/')
    else:
        # Credenciais inválidas
        return redirect('/accounts/flogin/?status=1')

def fazer_logout(request):
    logout(request)
    return redirect('/accounts/flogin/')

def gradeCurricular(request):
    periodos = Periodo.objects.all()
    print(periodos)  # Adicione esta linha para debug
    periodo_form = PeriodoForm()  # Adicionei isso para garantir que o formulário seja passado para o template
    disciplina_form = DisciplinaGForm()  # Adicionei isso para garantir que o formulário seja passado para o template
    return render(request, 'gradeCurricular.html', {'periodos': periodos, 'periodo_form': periodo_form, 'disciplina_form': disciplina_form})

def calendario(request, year=datetime.now().year, month=datetime.now().strftime('%B')):

    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    month = month.capitalize()
    cal = mark_safe(HTMLCalendar().formatmonth(year, month_number))

    #ano atual
    now = datetime.now() 

    #hora atual
    time = now.strftime("%H:%M %p")

    return render(request, 'usuarios:calendario.html', 
                  {
                    'year': year,
                    'month': month,
                    'month_number': month_number,
                    'cal': mark_safe(cal),
                    'time': time
                   })


def lista_eventos(request):
    eventos_lista = Evento.objects.filter(usuario=request.user).order_by('data_evento')
    return render(request, 'lista_eventos.html', {'eventos_lista': eventos_lista})


def criar_evento(request):
    submitted = False

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user
            evento.save()
            return redirect('usuarios:lista_eventos')
    else:
        form = EventoForm

    return render(request, 'criar_evento.html', {'form': form, 'submitted': submitted})

def atualizar_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    form = EventoForm(request.POST or None, instance=evento)

    if form.is_valid():
        form.save()
        return redirect('usuarios:lista_eventos')

    return render(request, 'atualizar_evento.html', {'evento': evento, 
    'form': form})

def deletar_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    evento.delete()
    return redirect('usuarios:lista_eventos')

def adicionarPeriodo(request):
    if request.method == 'POST':
        periodo_form = PeriodoForm(request.POST)
        if periodo_form.is_valid():
            periodo_form.save()
            return redirect('usuarios:grade_curricular')
    else:
        periodo_form = PeriodoForm()

    return render(request, 'adicionar_periodo.html', {'periodo_form': periodo_form})

def adicionarDisciplina(request):
    if request.method == 'POST':
        disciplina_form = DisciplinaGForm(request.POST)
        if disciplina_form.is_valid():
            disciplina_form.save()
            return redirect('usuarios:grade_curricular')
    else:
        disciplina_form = DisciplinaGForm()

    return render(request, 'adicionar_disciplina.html', {'disciplina_form': disciplina_form})

def lista_disciplina(request):
    disciplina_lista = Disciplina.objects.filter(usuario=request.user).order_by('nome_disciplina')
    return render(request, 'lista_disciplina.html', {'disciplina_lista': disciplina_lista})

def cadastro_disciplina(request):
    submitted = False
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.usuario = request.user 
            form.save()
            return redirect('usuarios:lista_disciplina')
    else:
        form = DisciplinaForm
        if 'submitted' in request.GET:
            submitted = True

    form = DisciplinaForm
    return render(request, 'cadastro_disciplina.html', {'form': form, 'submitted': submitted})

def atualizar_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    form = DisciplinaForm(request.POST or None, instance=disciplina)

    if form.is_valid():
        form.save()
        return redirect('usuarios:lista_disciplina')

    return render(request, 'atualizar_disciplina.html', {'disciplina': disciplina, 
    'form': form})

def deletar_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    disciplina.delete()
    return redirect('usuarios:lista_disciplina')

def anexar_arquivo(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    #disciplina = get_object_or_404(Disciplina, id=disciplina_id)

    if request.method == 'POST':
        form = AnexoForm(request.POST, request.FILES)
        if form.is_valid():
            anexo = form.save(commit=False)
            anexo.disciplina = disciplina
            anexo.usuario = request.user
            anexo.save()
            
            
            return redirect('usuarios:lista_disciplina')  
        else:
            form = AnexoForm()
    return render(request, 'anexar_arquivo.html', {'form': form, 'disciplina': disciplina})

def acessar_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    anexos = Anexo.objects.filter(disciplina=disciplina)
    return render(request, 'acessar_disciplina.html', {'disciplina': disciplina, 'anexos': anexos})

def adicionar_anotacao(request, disciplina_id):
    if request.method == 'POST':
        form = AnotacaoForm(request.POST)
        if form.is_valid():
            anotacao = form.save(commit=False)
            anotacao.usuario = request.user
            anotacao.disciplina_id = disciplina_id
            anotacao.save()
            return redirect('usuarios:lista_disciplina')
    else:
        form = AnotacaoForm()
    return render(request, 'adicionar_anotacao.html', {'form': form})