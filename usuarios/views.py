from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

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
        return redirect('/paginaInicial/')
    
def paginaInicial(request):
    return render(request, 'paginaInicial.html')

def menu(request):
    return render(request, 'menu.html')

def gradeCurricular(request):
    grade_curricular = [
        {
            'numero': 1,
            'disciplinas': [
                {'nome': 'Disciplina 1.1'},
                {'nome': 'Disciplina 1.2'},
            ]
        },
        {
            'numero': 2,
            'disciplinas': [
                {'nome': 'Disciplina 2.1'},
                {'nome': 'Disciplina 2.2'},
            ]
        },
    ]
    return render(request, 'gradeCurricular.html', {'grade_curricular': grade_curricular})




