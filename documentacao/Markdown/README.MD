## Dcomentação da pasta App
   
   - Pasta onde a aplicação fica,o projeto tem diversas pasta dentro dela
   a pasta onde fica os HTML que se chama 'templates', tem a pasta dos arquivos estaticos que se chama 'static', tem a pasta urls, ela é onde fica a logica de acesso da url da aplicação, tem a pasta da views, ela é a mais importanto pois fica a logica de negocio da aplicação do projeto, onde tem as funções e etc..., tem o arquivo Models, onde fica o modela do banco de dados, e tem o arquivo do admins, onde fica a parte do admin do projeto
    
## Documentação sobre a pasta static

   - Pasta static é onde fica o arquivo estatico da aplicação, tem 3 pasta dentro dela, onde se chama css, icones e js(Javascript)

        - Pasta css é onde fica o style dos HMTL, tem 8 pastas dentro dele, tem a pasta compras, onde fica os .css.
            
    ## Pasta css/compras

                - Pasta compras tem os arquivos do HTML compras    
                
                - dashboard.css pertence ao dashboard.hmtl da pasta template/compras/

                - Devolucao.css pertence a devolucao.css da pasta template/compras/

                - menuVendas.css pertence a menuVenda.html da pasta template/compras/

                - venda.css pertence a venda.html da pasta template/compras/

            ## Pasta css/dashboard

                - Pasta dashboard do css, só tem um arquivo css que
                pertence a dashboard.html, que o arquivo está no 
                templates/dashboard/
            
            - Pasta css/empresa
               
                - Pasta empresa tem 4 arquivos .css, onde pertence as arquivos da pasta templates/empresa
                    
                    - adicionarCliente.css pertence ao adicionarCliente.html da pasta templates/empresa/

                    - fornecedor.css pertence ao fornecedor.html da pasta templates/empresa/

                    - historicoDeEntregas.css pertence ao historicoDeEntregas.html da pasta templates/empresa/

                    - menuEmpresa.css pertence ao menuEmpresa.html da pasta templates/empresa/
            
    ## Pasta css/estoque
                
                - Pasta tem 4 arquivos de style onde pertence a pasta templates/estoque
                     
                    - adicionar.css pertence ao adicionar.html da pasta templates/estoque

                    - descricao.css pertence ao descricao.html da pasta templates/estoque

                    - editar.css pertence ao editar.html da pasta templates/estoque

                    - estoque.css pertence ao estoque.html da pasta templates/estoque
            
    ## Pasta css/financas

                - Pasta css/financas tem 6 arquivos de style que pertence a templates/financas
                    
                    - descricaoFatura.css pertence ao descricaoFatura.html da pasta templates/financas

                    - emitirNotasFiscais.css pertence ao emitirNotasFiscais.html da pasta templates/financas

                    - inserirFatura.css pertence ao inserirFatura.html da pasta templates/financas

                    - menuFinanca.css pertence ao manuFinanca.html da pasta templates/financas

                    -pagamento.css pertence ao pagamento.html da pasta templates/financas

                    - verFaturaVer.css pertence ao verFatura.html da pasta templates/financas

    ## Pasta css/login 
               
               - Pasta css/login tem 2 arquivos de style que pertence a    templates/login 
                  
                    - login.css pertence ao login.html da pasta templates/login
                    
                    ** esse arquivo de erro.html e erro.css não estão sendo utilizados na aplicação no momento
                    - erro.css pertence ao erro.html da pasta templates/login
            
    ## Pasta css/menu 

                - Pasta css/menu tem 1 arquivo que pertence ao templates/menus
                   
                    - menu.css pertence ao menu.html da pasta templates/menus
            
    ## Pasta css/usuario
                
                - Pasta css/usuario tem 1 arquivo de style que pertence a templates/menus

                    - usuario.css pertence ao usuario.html da pasta templates/usuario
        
    ## Pasta icones 

        - Essa é a pasta onde fica os icones ou imagens da aplicação web. Não tem muito o que descrever sobre ela


    ## Pasta js(Javascript)

        - Falando um pouco, essa é a pasta que fica os codigo em javascript da aplicação, ela tem 2 pasta dentro dela
                
            - js/empresa
                      
                - empresa/adicionarCliente.js pertence a pasta templates/empresa/adicionarCliente.html

                - fornecedor.js pertence a pasta templates/empresa/fornecedor.html
                
            - js/usuario
                    
                - usuario.js pertence a pasta templates/usuario/usuario.html

## Documentação sobre os arquivos Urls
    Urls é uma pasta que junta diversos arquivos de urls das funções,
    onde tem 7 arquivos de urls, elas fazem a logica de chamada de 
    função da views da aplicação

## Vamos falar dos arquivos
   - Views de arquivo

    ## urlsLogin
    
        Ele é a primeira urls a ser chamada pelo 
        usuario, onde está a função da urls sem 
        nada entre '', apelidada de login

        - ''
            Essa urls é a primeira a ser executada ou 
            chamada, ela não tem uma / com nome, ela é 
            a primeira. Essa urls chama a função de 
            LoginUser do arquivo viewsLogin.
        
        - '/home'
            Essa urls é a segunda a ser acessada ou chamada 
            por ser a urls do menu do site, caso o usuario 
            for logado certo, ele ir ser direcionada para 
            essa url, ela chama a função home do arquivo 
            viewsLogin.
        
        - 'acessoNegado/'
            Essa urls não está sendo usada pois é para erro de acesso
            negado, ela tem a função de redirecionar para um template
            que fala que acesso foi negado, ele chama a função 
            erroAcessoUrls do arquivo viewsLogin.
    
    ## urlEstoque
        
        Ele é a url da parte que abriga o estoque do sistema,
        ele tem 5 url para controlar a parte de backend do viewsEstoque,
        sempre vai aparecer o '/estoque/' e dps vem o nome da url