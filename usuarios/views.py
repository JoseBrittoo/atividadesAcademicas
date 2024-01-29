from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario, Evento, Disciplina
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Evento, Periodo
from .forms import EventoForm, PeriodoForm, DisciplinaGForm, DisciplinaForm, AnexoForm
from django.contrib.auth.decorators import login_required 



def home(request):
    return render(request, 'home.html')

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def acessar_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    return render(request, 'acessar_disciplina.html', {'disciplina': disciplina})

def novatarefa(request):
    status = request.GET.get('status')
    return render(request, 'novatarefa.html', {'status': status})

def paginaInicial(request):
    return render(request, 'paginaInicial.html')

def menu(request):
    return render(request, 'menu.html')

def valida_cadastro(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(email = email)

    #verifica se o email está vazios
    if len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    #verifica se o email já existe
    if len(usuario) > 0: 
        return redirect('/auth/cadastro/?status=3')
    
    try: 
        usuario = Usuario(email = email, senha = senha)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')
    
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')  

    usuario = Usuario.objects.filter(email = email, senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('paginaInicial')
    
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
    cal = HTMLCalendar().formatmonth(year, month_number)

    #ano atual
    now = datetime.now() 

    #hora atual
    time = now.strftime("%H:%M %p")

    return render(request, 'calendario.html', 
                  {
                    'year': year,
                    'month': month,
                    'month_number': month_number,
                    'cal': cal,
                    'time': time
                   })

#@login_required(login_url='/auth/login/')
def lista_eventos(request):
    eventos_lista = Evento.objects.all().order_by('data_evento')
    return render(request, 'lista_eventos.html', {'eventos_lista': eventos_lista})

#@login_required(login_url='/auth/login/')
def criar_evento(request):
    submitted = False
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/auth/criar_evento?submitted=True')
    else:
        form = EventoForm
        if 'submitted' in request.GET:
            submitted = True

    form = EventoForm
    return render(request, 'criar_evento.html', {'form': form, 'submitted': submitted})

def atualizar_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    form = EventoForm(request.POST or None, instance=evento)

    if form.is_valid():
        form.save()
        return redirect('lista_eventos')

    return render(request, 'atualizar_evento.html', {'evento': evento, 
    'form': form})

def deletar_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    evento.delete()
    return redirect('lista_eventos')

def adicionarPeriodo(request):
    if request.method == 'POST':
        periodo_form = PeriodoForm(request.POST)
        if periodo_form.is_valid():
            periodo_form.save()
            return redirect('grade_curricular')
    else:
        periodo_form = PeriodoForm()

    return render(request, 'adicionar_periodo.html', {'periodo_form': periodo_form})

def adicionarDisciplina(request):
    if request.method == 'POST':
        disciplina_form = DisciplinaGForm(request.POST)
        if disciplina_form.is_valid():
            disciplina_form.save()
            return redirect('grade_curricular')
    else:
        disciplina_form = DisciplinaGForm()

    return render(request, 'adicionar_disciplina.html', {'disciplina_form': disciplina_form})

def lista_disciplina(request):
    disciplina_lista = Disciplina.objects.all().order_by('nome_disciplina')
    return render(request, 'lista_disciplina.html', {'disciplina_lista': disciplina_lista})

def cadastro_disciplina(request):
    submitted = False
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/auth/cadastro_disciplina?submitted=True')
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
        return redirect('lista_disciplina')

    return render(request, 'atualizar_disciplina.html', {'disciplina': disciplina, 
    'form': form})

def deletar_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    disciplina.delete()
    return redirect('lista_disciplina')

def anexar_arquivo(request, disciplina_id):
    #disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)

    if request.method == 'POST':
        form = AnexoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            anexo = form.save(commit=False)
            anexo.disciplina = disciplina
            anexo.save()
            
            return redirect('cadastro_disciplina')  
    return render(request, 'anexar_arquivo.html', {'form': form, 'disciplina': disciplina})
