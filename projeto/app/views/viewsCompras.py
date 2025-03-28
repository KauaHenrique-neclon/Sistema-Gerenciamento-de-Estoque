from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from app.models import Produto , SaidaMercadoria, Cliente, Devolucao
import datetime
from app.views.viewsLogin import verificar_login

################
### função de vendas
@verificar_login
def index(request):
    if request.method == 'POST':
        idproduto = request.POST.get('id_produto')
        quantidade = request.POST.get('quantidade')
        valor = request.POST.get('valor')
        if quantidade and valor:
            try:
                venda = SaidaMercadoria(
                    quantidade = quantidade,
                    valor = valor,
                    datacompra = datetime.date.today,
                    idproduto = idproduto
                )
                venda.save()
                # ele altera o banco de produto caso a venda seja feita
                produtoModel = get_object_or_404(Produto, idproduto=idproduto)
                quantidadeUpdrate = produtoModel.quantidade - quantidade
                produtoModel.quantidade = quantidadeUpdrate
                produtoModel.save()
                return messages.success(request, 'Cadastrada com sucesso')
            except:
                return messages.error(request, 'Erro ao salvar dados')
        else:
            return messages.error(request, 'Preencha todos os dados')
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'compras/venda.html',contexto)

###############
##### função de dashboard de vendas
@verificar_login
def estatisticasVendas(request):
    dataHoje = datetime.date.today()
    saida = SaidaMercadoria.objects.filter(datacompra=dataHoje).count()
    cliente = Cliente.objects.count()
    try:
        totalValor = SaidaMercadoria.objects.filter(datacompra=dataHoje).aaggregate(total=sum('valor'))['total'] or 0
    except (TypeError, ValueError):
        totalValor = 0
    contexto = {
        'saida': saida,
        'valor': totalValor,
        'cliente': cliente,
    }
    return render(request, 'compras/dashboard.html',  contexto)

#########
## função de cadastro de devolução
@verificar_login
def devolucao(request):
    if request.method == 'POST':
        idproduto = request.POST.get('id_produto')
        if idproduto:
            quantidadeDevolucao = request.POST.get('quantidade')
            motivo = request.POST.get('motivo')
            if quantidadeDevolucao and motivo:
                try:
                    dadosProduto = Produto.objects.filter(idproduto=idproduto).first()
                    novaDevolucao = Devolucao(
                        quantidade = quantidadeDevolucao,
                        motivo = motivo,
                        valor = dadosProduto.preco * quantidadeDevolucao,
                        idproduto = idproduto
                    )
                    novaDevolucao.save()
                    if motivo == 'decisao' or 'naoGostou':
                        alterarProduto = Produto(
                            idproduto = idproduto,
                            quantidade = Produto.quantidade + quantidadeDevolucao
                        )
                        alterarProduto.save()
                        messages.success(request, 'Devolução cadastrada e salvo o estoque Produto')
                    else:
                        messages.error(request,'Devolução cadastrada')
                except:
                    messages.error(request,'Erro no banco de dados')
    produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, 'compras/devolucao.html', contexto)