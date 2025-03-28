from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #para pedir login e evitar acesso não autorizado
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib import messages
import datetime
#from pynfe.processamento import NFeProcessor
from app.models import Fatura, Pagamento, Financas, NotaFiscal
from app.views.viewsLogin import verificar_login

@verificar_login
def InserirFatura(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        valor = request.POST.get('valor')
        codigoDeBarra = request.POST.get('codigoDeBarra')
        status = request.POST.get('status')
        if data and valor and codigoDeBarra and status:
            novoFatura = Fatura(
                data = data,
                valor = valor,
                codigoDeBarra = codigoDeBarra,
                status = status
            )
            novoFatura.save()
        else:
            return messages.error(request, 'Erro ao inserir no banco de dados')
    return render(request, 'financas/inserirFatura.html')

@verificar_login
def pagamentosFaturas(request):
    if request.method == 'POST':
        formaDePagamento = request.POST.get('forma')
        codigoDeBarraPagina = request.POST.get('idFatura')
        if formaDePagamento and codigoDeBarraPagina:
            registrarPagaamento = Pagamento(
                data = datetime.date.today,
                codigoDeBarraFatura = codigoDeBarraPagina,
                formaDePagamento = formaDePagamento
            )
            registrarPagaamento.save()
        else:
            return messages.error(request, 'Preencha todos os campos')
    faturas = Fatura.objects.filter(status='pedente')
    contexto = {'faturas': faturas}
    return render(request, 'financas/pagamento.html', contexto)

@verificar_login
def verFaturas(request):
    statusFatura = request.GET.get('status')
    totalFatura = []
    contexto = {}
    if statusFatura:
        try:
           totalFatura = Fatura.objects.filter(status=statusFatura)
           contexto = {'totalFatura':totalFatura}
        except:
            messages.error(request, 'Erro ao obter faturas')
    if contexto:
        contexto = {'totalFatura':totalFatura}
    return render(request, 'financas/verFatura.html',contexto)

@verificar_login
def descricaoFatura(request):
    codigoBarra = request.POST.get('PegarCodigoDeBarra')
    dadosFatura = Fatura.objects.filter(codigoDeBarra=codigoBarra).first()
    contexto = {'dadosFatura':dadosFatura}
    return render(request, 'financas/descricaoFatura.html',contexto)

"""
@verificar_login
def emitirNotas(request):
    if request.method == 'POST':
        cnpjEmitente = request.POST.get('cnpj_emitente')
        cnpjDestinatario = request.POST.get('cnpj_destinatario')
        valor = request.POST.get('valor')
        if cnpjDestinatario and cnpjEmitente and valor:
            try:
                novaNotaFiscal = NotaFiscal(
                    cnpj_emitente = cnpjEmitente,
                    cnpj_destinatario = cnpjDestinatario,
                    valor = valor,
                )
                novaNotaFiscal.save()
                notaFiscal = {
                    'emitente': {
                        'CNPJ': cnpjEmitente,
                    },
                    'destinatario': {
                        'CNPJ': cnpjDestinatario,
                    },
                    'valor': valor,
                    'data de emissão':datetime.date.today()
                }
                processar = NFeProcessor()
                try:
                    response = processar.emit(notaFiscal)
                    if response['status'] == 'Aprovado':
                        novaNotaFiscal.chave_nfe = response['chave']
                        novaNotaFiscal.status = response['status']
                        novaNotaFiscal.save()
                        messages.success(request, 'Nota fiscal emitida com sucesso.')
                    else:
                        messages.error(request, f'Erro ao emitir: {response.get("mensagem")}')
                except Exception as e:
                    messages.error(request, f'Ocorreu um erro: {str(e)}')
            except Exception as e:
                messages.error(request, f'Ocorreu um erro: {str(e)}')
    return render(request, 'financas/emitirNotasFiscais.html')"
    """