# desafio_itflex


Esse projeto fui criado utilizando o framework django junto com a linguagem de programação python e banco de dados mysql.

Para funcionamento correto do mesmo é necessário fazer instalação das seguintes aplicações (instalação realizada utilizando comando apt linux ubuntu).
- python-django
- python-djangorestframework
- python-mysqldb

Cria banco de dados:
Aplicação está configurada para conectar ao banco com usuário root sem senha.
Caso deseja alterar a configuração, edite o arquivo setting.py que fica dentro do diretório agenda.
No parâmetro DATABASES altere as configurações do banco de dadods para o desejado.
Caso queira utilizar as configurações pré-configuradas, crie o banco chamado agenda.

Starting o projeto agenda:
Caminha para o diretorio desafio_itflex e digite o seguinte comandos:
- // Comando para sicronizar entidades do projeto com banco de dados. Esse comando que cria tabelas no DB.
 
- // Iniciando servidor django na porta 8000
- python manage.py runserver 

Testando a aplicação:
Para testar aplicação por interface gráfica acesse o seguinte link:
http://localhost:8000/tarefas

Para testar API Rest Task execute o seguintes comandos abaixo:
Inserir resgistro?
- curl -X POST -H "Content-Type: application/json" -d '{"task": "TESTE REST1", "done":0}' http://localhost:8000/task/

Ler registros:
- curl http://localhost:8000/task/
