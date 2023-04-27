# Sistema de Gerenciamento de Produtos

Este projeto é uma API simples para gerenciar produtos usando Python, Flask e SQLite. Ele permite criar, atualizar, buscar e remover produtos no banco de dados.

## Arquitetura e Composição

### Modelos

O arquivo `modelos.py` define a estrutura do banco de dados SQLite e cria uma tabela chamada `produtos` com as seguintes colunas:

- id: chave primária, identificador único para cada produto
- nome: nome do produto (texto)
- descricao: descrição do produto (texto)
- preco: preço do produto (número real)

### Rotas

O arquivo `rotas.py` contém as rotas da API e suas funções correspondentes. As seguintes rotas estão disponíveis:

1. `GET /produtos`: busca todos os produtos
2. `GET /produtos/<produto_id>`: busca um produto específico pelo ID
3. `POST /produtos`: cria um novo produto
4. `PUT /produtos/<produto_id>`: atualiza um produto específico pelo ID
5. `DELETE /produtos/<produto_id>`: remove um produto específico pelo ID
6. `DELETE /produtos`: remove todos os produtos

### Client

O arquivo `client.py` é um exemplo de cliente Python que utiliza a biblioteca `requests` para interagir com a API. Você pode utilizar o Postman, se preferir, a partir das rotas.

### main.py

Este arquivo é usado para iniciar a aplicação Flask.

## Testes

O arquivo `test.py` contém testes unitários para a API usando a biblioteca `unittest`. Os seguintes testes estão incluídos:

1. `test_criar_produto`: Testa a criação de um novo produto
2. `test_buscar_produtos`: Testa a busca de todos os produtos
3. `test_buscar_produto`: Testa a busca de um produto específico pelo ID
4. `test_atualizar_produto`: Testa a atualização de um produto específico pelo ID
5. `test_remover_produto`: Testa a remoção de um produto específico pelo ID
6. `test_remover_todos_produtos`: Testa a remoção de todos os produtos

### Como executar os testes

Para executar os testes, instale as dependências necessárias:

pip install Flask
pip install requests
Em seguida, execute o arquivo `test.py`:
python test.py


Os resultados dos testes serão exibidos no terminal.


### Executando o projeto
Siga os passos abaixo para executar o projeto em seu ambiente local:

1. Instalação das dependências
Antes de executar o projeto, é necessário instalar as dependências necessárias. No terminal, navegue até a pasta do projeto e execute o seguinte comando:

pip install -r requirements.txt

Isso instalará todas as dependências listadas no arquivo requirements.txt.

### Popular o banco de dados
Para adicionar produtos de exemplo ao banco de dados, execute o seguinte comando no terminal:

python add_produtos.py

Esse comando executará o arquivo que insere os produtos de exemplo no banco de dados SQLite.

### Executar a aplicação Flask
Agora você pode executar o servidor de aplicativos Flask. No terminal, execute o seguinte comando:

python main.py

Isso iniciará o servidor Flask no endereço http://localhost:5000. Agora você pode acessar a API usando um navegador, um cliente REST como o Postman ou o aplicativo client.py fornecido.
