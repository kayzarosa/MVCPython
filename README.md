## MVC Person e Pets

# :rocket: Back-End

> TUDO ESTÁ BEM!!!!!.  <img src="https://user-images.githubusercontent.com/20192309/80777643-4202cd80-8b3c-11ea-8f32-5348bda4486b.jpg" width="10%" />

# Sobre a api

## Resumo da api

Um sistema de cadastro de pessoas e seus pets adotados. Utilizando um bando de dados SqlLite para salvar as informaçãos.
O projeto foi feito em cima da arquitura MVC separando as responsábilidades e ao mesmo tempo criando testes para validar as funcionalidades.

## Dependências

Para trabalhar com as dependências do python é interessante criar um ambiente virtual com o seguinte comando:

````sh
pip3 install virtualenv
````
Após executar o comando e o mesmo retornando sucesso, agora vamos entrar na pasta do projeto e abrir o terminal e executar o seguinte comando:

````sh
python3 -m venv venv 
````
Para ativar a máquina virtual executamos o comando abaixo.

````sh
source venv/bin/activate
````

Pronto ambiente virtual criado e ativado, caso queira ter certeza que o mesmo está ativo é só executar o comando:

````sh
pip freeze
````

E vamos instalar as depenências:

````sh
pip3 install -r requirements.txt
````

Para confirmar se as dependências foram instaladas corretamente é executar o comando <b>pip freeze</b> que irá trazer a lista. 

Para rodar o projeto e utilizar as rotas é só executar o comando:

````sh
python3 run.py
````

E para verificar se os testes estão passando é só executar o comando:


````sh
pytest -s -v
````


E para desativar esse ambiente virtual você pode fechar o terminal então tome cuidado, pois se fechar sem querer o seu projeto pode não funcionar mais. 

Para finalizar o ambiente virtual execute o comando:

````sh
deactivate
````

Feito com ♥ by Kayza :wave:
