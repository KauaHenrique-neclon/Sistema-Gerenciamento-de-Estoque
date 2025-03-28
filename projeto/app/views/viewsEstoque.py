from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #para pedir login e evitar acesso não autorizado
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
import logging
from django.contrib import messages
from app.models import Usuario , Produto
from django.contrib.auth.hashers import check_password
import datetime
from app.views.viewsLogin import verificar_login


### função do menu do estoque
#####
@verificar_login
def estoque(request):
    produtos = Produto.objects.filter(is_active=True)
    contexto = {'produtos': produtos}
    return render(request, 'estoque/estoque.html', contexto)

### função de deixar falso o produto, mas não tem html
#####
@verificar_login
def deletarProduto(request):
    if request.method == 'POST':
        idproduto = request.POST.get('idprodutodelete')
        if idproduto:
            isDesativar = Produto(
                idproduto = idproduto,
                is_active = False
            )
            isDesativar.save()
            messages.success(request, 'Desativado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro em desativar produto')
    else:
        messages.error(request, 'methodo não permitido')

### função de ver o dados completo do produto
#####
@verificar_login
def descricaoProduto(request):
    idproduto = request.POST.get('idprodutodescricao')
    descricao = Produto.objects.filter(idproduto=idproduto).first()
    contexto = {'descricao': descricao}
    return render(request, 'estoque/descricao.html',contexto)

### função de editar o produto
######
@verificar_login
def editarProduto(request):
    idproduto = request.POST.get('idprodutoeditar')
    dadosprodutos = Produto.objects.filter(idproduto=idproduto).first()
    dados = {'dados': dadosprodutos}
    return render(request, 'estoque/editar.html', dados)

def editarInfoProduto(request):
    if request.method == 'POST':
        idDoProduto = request.POST.get('dadosIdProduto')
        if idDoProduto:
            descricaoRecebido = request.POST.get('descricaoi')
            precoRecebido = request.POST.get('precoi')
            quantidadeRecebido = request.POST.get('quantidadei')
            controladoRecebido = request.POST.get('controladoi')
            if controladoRecebido and descricaoRecebido and precoRecebido and quantidadeRecebido:
                ## buscando os dados do produto atraves do id
                updateProduto = Produto.objects.get(idproduto = idDoProduto)
                ## salvando os novos dados
                updateProduto.preco = precoRecebido
                updateProduto.descricao = descricaoRecebido
                updateProduto.quantidade = quantidadeRecebido
                updateProduto.controlado = controladoRecebido
                updateProduto.save()
                messages.success(request, 'Atualizado com sucesso')
                return redirect('estoque')
            else:
                messages.error(request, 'Erro em atualizar os dados')
        else:
            messages.error(request, 'erro ao receber o id do produto')
    else:
        messages.error(request, 'method não aceito')

### função de adicionar produtos
#########
@verificar_login
def adicionarProdutos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        controlado = request.POST.get('controlado')
        if nome and descricao and preco and quantidade and controlado:
            try:
                produtoNovo = Produto(
                    nome=nome,
                    descricao=descricao,
                    preco=preco,
                    quantidade=quantidade,
                    controlado=controlado
                )
                produtoNovo.save()
                messages.success(request, 'Produto adicionado com sucesso!')  
                return redirect('estoque')
            except:
                messages.error(request, 'Erro ao adicionar')
        else:
            messages.error(request, 'Preencha todos os dados necessario')
    return render(request, 'estoque/adicionar.html')