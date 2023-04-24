import sqlite3

BANCO_DE_DADOS = "produtos.db"

produtos_exemplo = [
    {
        "nome": "Produto 1",
        "descricao": "Este é o Produto 1.",
        "preco": 19.99
    },
    {
        "nome": "Produto 2",
        "descricao": "Este é o Produto 2.",
        "preco": 29.99
    },
    {
        "nome": "Produto 3",
        "descricao": "Este é o Produto 3.",
        "preco": 39.99
    }
]

conexao = sqlite3.connect(BANCO_DE_DADOS)
cursor = conexao.cursor()

for produto in produtos_exemplo:
    cursor.execute("INSERT INTO produtos (nome, descricao, preco) VALUES (?, ?, ?)",
    (produto["nome"], produto["descricao"], produto["preco"]))

conexao.commit()
conexao.close()

print("Produtos de exemplo adicionados ao banco de dados.")
