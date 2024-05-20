Funcionalidade: Acessar a API do Github com o dado de um usuario

Cenario: Obter os dados do usuario na pagina da API do Github  

  Dado eu esteja na pagina da API do Github 
  Quando eu digito o nome do usuario na URL https://api.github.com/users/
  Entao vejo os dados Nome, Repositorios Publicos, Following, Followers

Cenario: Obter os dados dos Repositorios do usuario   

  Dado eu esteja na pagina do usuario da API do Github 
  Quando eu digito repos na URL https://api.github.com/users/
  Entao vejo as informacoes dos repositorios publicos do usuario como URL e nomes dos repositorios

Cenario: Gerar o relatorio do usuario   

  Dado eu esteja no relatorio do usuario 
  Quando eu visualizo o nome do arquivo usuario.txt com o mesmo nome do usuario 
  E verifico a mensagem que usuario nao possui nenhum Repositorio
  OU quando usuario possui repositorios publicos  
  Entao verifico a lista dos repositorios publicos com nome e URL
  E verifico as informacoes: Nome, Perfil, Número de repositórios publicos, Número de seguidores, Número de usuários seguidos
