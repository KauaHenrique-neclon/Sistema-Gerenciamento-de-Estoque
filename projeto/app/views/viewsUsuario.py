from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Usuario
import re
from app.views.viewsLogin import verificar_login

@verificar_login
def criarUsuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        PrimeiroName = request.POST.get('firshName')
        UltimoName = request.POST.get('lastName')
        padrão = r"^[a-zA-Z0-9._%+-]+@[gmail.-]+\.(com)$"
        if re.match(padrão, nome, re.IGNORECASE):
            if len(senha) >= 8 and senha.isdigit():
                if nome and senha and PrimeiroName and UltimoName:    
                    try:
                        novoUsuario = Usuario(
                            username = nome,
                            password = senha,
                            first_name = PrimeiroName,
                            last_name = UltimoName
                        )
                        novoUsuario.save()
                        messages.success(request, 'Usuario criado')
                        return redirect('home')
                    except:
                        messages.error(request, 'Erro ao criar um usuario')
                else:
                    messages.error(request, 'Preencha todos os dados necessarios')
            else:
                messages.error(request, 'Senha deve ter mais de 8 caracteres')
        else:
            return messages.error(request, 'Deve ser email')
    dadosUsuario = Usuario.objects.all()
    contexto = {'usuario':dadosUsuario}
    return render(request, 'usuario/usuario.html', contexto)