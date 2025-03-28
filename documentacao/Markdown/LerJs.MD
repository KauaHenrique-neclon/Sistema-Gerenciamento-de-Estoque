## descrição dos codigos em Javascripts
documentação das arquivos feitos em js(javascript)

## descrição
    - Este código JavaScript manipula a exibição
    de dois elementos HTML:um para adicionar 
    números de CPF e outro para adicionar números 
    de CNPJ. Ele alterna a visibilidade desses 
    elementos com base nas ações do usuário,
     ou seja, ao clicar em botões correspondentes.


## Dependências adiconarCliente.js
    ## HTML com os IDs:
    * adicionarCPF
    * buttonAdicionarCPF
    * adicionarCNPJ
    * buttonAdicionarCNPJ

    ## Variáveis
    - adicionarCPF: Armazena o elemento HTML que 
    representa a seção para adicionar CPF.

    - buttonAdicionarCPF: Armazena o botão que,
    quando clicado, exibe a seção para 
    adicionar CPF. 

    - adicionarCNPJ: Armazena o elemento HTML 
    que representa a seção para adicionar CNPJ.

    - buttonAdicionarCNPJ: Armazena o botão que, 
    quando clicado, exibe a seção para adicionar 
    CNPJ.


    ## Eventos
    buttonAdicionarCPF.addEventListener("click",...)

    -- Ao clicar no botão buttonAdicionarCPF:
    Verifica se a seção adicionarCPF já está 
    visível (estilo display igual a "block").
    Se estiver visível, mantém-a visível.

    Caso contrário, exibe a seção adicionarCPF e 
    oculta a seção adicionarCNPJ.

    buttonAdicionarCNPJ.addEventListener("click", ...)

    Ao clicar no botão buttonAdicionarCNPJ:
    Verifica se a seção adicionarCNPJ já está visível.
    Se estiver, mantém-a visível.
    Caso contrário, exibe a seção adicionarCNPJ 
    e oculta a seção adicionarCPF.

## Dependências fornecedor.js

    ## HTML com os seguintes IDs:

        * cadastro (para a seção de cadastro de fornecedor)
        * buttonCadastar (botão para mostrar a seção de cadastro de fornecedor)
        * recebimento (para a seção de recebimento)
        * buttonEntregas (botão para mostrar a seção de recebimento)

    ## Variáveis
        * adicionarFornecedor: Armazena o elemento 
        HTML que representa a seção para adicionar 
        fornecedores.

        * buttonAdicionarFornecedor: Armazena o botão
         que, ao ser clicado, exibe a seção para 
         adicionar fornecedores.

        * adicionarEntrega: Armazena o elemento HTML 
        que representa a seção para registro de 
        recebimento.

        * buttonAdicionarEntrega: Armazena o botão 
        que, ao ser clicado, exibe a seção para 
        registro de recebimento.

    ## Eventos

        buttonAdicionarFornecedor.addEventListener("click", ...)

        Ao clicar no botão buttonAdicionarFornecedor:
        Verifica se a seção adicionarFornecedor já está
         visível (com o estilo display igual a "block").
        Se estiver visível, mantém a visibilidade.
        Caso contrário, exibe a seção adicionarFornecedor
         e oculta a seção adicionarEntrega.

        buttonAdicionarEntrega.addEventListener("click", ...)

        Ao clicar no botão buttonAdicionarEntrega:
        Verifica se a seção adicionarEntrega já 
        está visível.
        Se estiver visível, mantém a visibilidade.
        Caso contrário, exibe a seção adicionarEntrega 
        e oculta a seção adicionarFornecedor.