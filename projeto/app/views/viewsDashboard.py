from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Cliente, Produto, Fornecedor, RecebimentoMercadoria, SaidaMercadoria
from app.views.viewsLogin import verificar_login

################
### função de dashboard do sisteme
@verificar_login
def dashboard(request):
    totalClinte = Cliente.objects.count()
    totalProdutos = Produto.objects.count()
    totalFornecedor = Fornecedor.objects.count()
    ultimasTresVendas = SaidaMercadoria.objects.order_by('-datacompra')[:3]
    dados = {
        'totalCliente': totalClinte,
        'totalProdutos': totalProdutos,
        'totalFornecedor': totalFornecedor,
        'ultimasTresVendas': ultimasTresVendas,
    }
    return render(request, 'dashboard/dashboard.html',dados)