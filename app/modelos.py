import sqlite3

BANCO_DE_DADOS = "produtos.db"

conexao = sqlite3.connect(BANCO_DE_DADOS)
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        preco REAL NOT NULL
    );
""")

conexao.commit()
conexao.close()
