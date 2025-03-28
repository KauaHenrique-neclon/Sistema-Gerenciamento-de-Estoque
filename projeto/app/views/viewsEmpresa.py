from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
import requests
from app.models import Cliente, Produto, Fornecedor, RecebimentoMercadoria
from app.views.viewsLogin import verificar_login

# função para adicionar cliente por CPF ou CNPJ
@verificar_login
def adicionarClientes(request):
    if 'adicionarCPF' in request.POST:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        if nome and sobrenome and telefone and email and bairro and rua and numero:
            if len(cpf) == 11:
                try:
                    novoClienteCpf = Cliente(
                        nome = nome,
                        sobrenome = sobrenome,
                        telefone = telefone,
                        cpf = cpf,
                        email = email,
                        bairro = bairro,
                        rua = rua,
                        numero = numero
                    )
                    novoClienteCpf.save()
                    return messages.success(request, 'Adicionado com sucesso')
                except:
                    return messages.error(request, 'Erro ao adicionar cliente')
            else:
                return messages.error(request, 'Preencha os 11 digitos do CPF')
        else:
            return messages.error(request, 'Preencha todos os dados necessario')
    elif 'adicionarCNPJ' in request.POST:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        telefone = request.POST.get('telefone')
        cnpj = request.POST.get('cnpj')
        email = request.POST.get('email')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        if nome and sobrenome and telefone and email and bairro and rua and numero:
            if len(cnpj) == 14:
                if cnpj:
                    #verifica se o CNPJ é ativo ou não
                    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
                    response = requests.get(url)
                    data = response.json()
                    if 'status' in data and data['status'] == 'ERROR':
                        return False, data['message']
                    
                    #salva o dados dados o CPNJ foi ativo
                    try:
                        novoClienteCnpj = Cliente(
                        nome = nome,
                        sobrenome = sobrenome,
                        telefone = telefone,
                        cnpj = cnpj,
                        email = email,
                        bairro = bairro,
                        rua = rua,
                        numero = numero
                        )
                        novoClienteCnpj.save()
                        messages.success(request, 'Adicionado com sucesso')
                        return redirect('AdicionarCliente')
                    except:
                        messages.error(request, 'Erro ao adicionar cliente')
                        return redirect('AdicionarCliente')
                else:
                    messages.error(request, 'Cliente não achado')
                    return redirect('AdicionarCliente')
            else:
                messages.error(request, 'Preencha os 14 digitos do CNPJ')
                return redirect('AdicionarCliente')
        else:
            messages.error(request, 'Preencha todos os dados necessarios')
            return redirect('AdicionarCliente')
    return render(request, 'empresa/adicionarCliente.html')

###
## função para desativar o cliente
@verificar_login
def desativarClientes(request):
    if request.method == 'POST':
        idCliente = request.POST.get('')
        if idCliente:
            desativarCliente = Cliente(
                idcliente = idCliente,
                is_active = False
            )
            desativarCliente.save()
            messages.error(request, 'Clinte desativado com sucesso')
            return redirect('MenuEmpresa')
        else:
            messages.error(request, 'Erro em desativar cliente')
            return redirect('desativarCliente')
    else:
        messages.error(request, 'methodo não permitido')
        return redirect('estoque')

#########
# função para cadastrar fornecedor
@verificar_login
def adicionarFornecedor(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('telefone')
        nomeEmpresa = request.POST.get('nomefornece')
        endereco = request.POST.get('endereco')
        bairro = request.POST.get('beirro')
        numero = request.POST.get('numero')
        if cnpj and telefone and nomeEmpresa and endereco and bairro and numero:
            novoFornecedor = Fornecedor(
                cnpj = cnpj,
                telefone = telefone,
                nomeEmpresa = nomeEmpresa,
                endereco = endereco,
                bairro = bairro,
                numero = numero
            )
            novoFornecedor.save()
            messages.success(request, 'Cadastrado com sucesso')
            return redirect('adicionarFornecedor')
    produtos = Produto.objects.all()
    contexto = {'produtos':produtos}
    return render(request, 'empresa/fornecedor.html', contexto)

######################
## função para cadastrar entregas recebidas
@verificar_login
def EntregasFeitas(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        totalRecebido = request.POST.get('totalproduto')
        notaFiscal = request.POST.get('notaFiscal')
        idproduto = request.POST.get('id_produto')
        cnpjFornecedor = Fornecedor.objects.filter(cnpj=cnpj).first()
        if cnpjFornecedor:
            if idproduto:
                if totalRecebido and notaFiscal and cnpj:
                    EntregaRecebida = RecebimentoMercadoria(
                        totalproduto = totalRecebido,
                        notaFiscal = notaFiscal,
                        cnpj = cnpj,
                        idproduto = idproduto
                    )
                    ## ele altera o banco do produto
                    EntregaRecebida.save()
                    produtoUpdade = get_object_or_404(Produto, idproduto=idproduto)
                    quantidateUpdate = produtoUpdade.quantidade + totalRecebido
                    produtoUpdade.quantidade = quantidateUpdate
                    produtoUpdade.save()
                    messages.success(request, 'Entrega salva')
                    return redirect('Entregas')
                else:
                    messages.error(request, 'Adicione todos os campos necessarios')
                    return redirect('Entregas')
            else:
                return messages.error(request,'Erro ao pegar Id do produto')
        else:
            return messages.error(request, 'Não tem um Fornecedor com esse CNPJ')


######
### função quee mostra o historico de entregas 
@verificar_login
def historiocoEntregas(request):
    mes = request.GET.get('mes')
    entregas = []
    contexto = {}
    if mes:
        try:
            entregas = RecebimentoMercadoria.objects.filter(datarecebeu=mes)
            contexto = {'entregas': entregas}
        except:
            messages.error(request, 'Erro ao obter entregas')
    if contexto == {}:
        contexto = {'entregas': entregas}
    return render(request, 'empresa/historicoDeEntregas.html', contexto)