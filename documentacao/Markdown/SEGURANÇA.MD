## Documentação de segurança do sistema

   - A seguraça foi feita atraves de uma função e é foi usada como decorador, no viewsLogin.py foi criado uma função chamada verificar_login, ela verifica se o idusuario ou request.session.get('user_id') está ativo ou longado, se não tiver, ele vai redirecionar para uma pagina de acesso negado, e ate fazer o login, ele vai rejeitar o acesso por URL.

   - Banco de dados que abriga os dados do login dos usuario, ele é o model Usuario, onde é verificado de maneira comum, ele busca os dados e verifica se tem no banco, se tiver, ele vai guarda o id do usuario numa request.session, onde vai ser usada em todo o sistema.