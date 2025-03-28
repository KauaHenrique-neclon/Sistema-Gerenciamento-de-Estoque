from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #para pedir login e evitar acesso não autorizado
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import logging
from django.contrib import messages
from app.models import Usuario , Produto
from django.contrib.auth.hashers import check_password
import datetime

def loginUser(request):
    if request.method == 'POST':
        usuario = request.POST['email']
        senha = request.POST['senha']
        print(usuario, senha)
        if not usuario or not senha:
            messages.error(request, 'Entre com usuario e senha')
            return redirect('login')
        #usuari = Usuario.objects.get(email=usuario)
        #user = authenticate(request, username=usuari.username, password=senha)
        user = Usuario.objects.filter(email=usuario).first()  # Supondo que email é um campo no modelo
        if user is not None and senha == user.password:
            request.session['user_id'] = user.idusuario
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Erro ao autenticar')
    return render(request, 'login/login.html')

def verificar_login(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('user_id'):
            return view_func(request, *args, **kwargs)
        
        else:
            return redirect('acessoNegado')
    return wrapper

### função do menu principal da aplicação
#####
#@login_required()
@verificar_login
def home(request):
    contexto = {}
    hora = datetime.datetime.now().strftime('%H:%M')
    contexto['hora'] = hora
    return render(request, 'menus/menu.html',contexto)


def erroAcessoUrls(request):
    #messages.error(request, 'Erro: Você não tem permissão para acessar esta página.')
    return render(request, 'login/erro.html')

def logout_view(request):
    logout(request)
    return redirect('login')