from flask import Flask, jsonify, request
from app.modelos import BANCO_DE_DADOS
import sqlite3

app = Flask(__name__)

@app.route('/produtos', methods=['GET'])
def buscar_produtos():
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    return jsonify(produtos)

@app.route('/produtos/<int:produto_id>', methods=['GET'])
def buscar_produto(produto_id):
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()
    conexao.close()
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"status": "erro", "mensagem": "Produto não encontrado."}), 404

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    nome = dados.get('nome', '')
    descricao = dados.get('descricao', '')
    preco = dados.get('preco', 0.0)
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, descricao, preco) VALUES (?, ?, ?)", (nome, descricao, preco))
    produto_id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return jsonify({"status": "sucesso", "mensagem": "Produto criado.", "id": produto_id})

@app.route('/produtos/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    dados = request.get_json()
    nome = dados.get('nome')
    descricao = dados.get('descricao')
    preco = dados.get('preco')
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    if nome:
        cursor.execute("UPDATE produtos SET nome = ? WHERE id = ?", (nome, produto_id))
    if descricao:
        cursor.execute("UPDATE produtos SET descricao = ? WHERE id = ?", (descricao, produto_id))
    if preco:
        cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (preco, produto_id))
    conexao.commit()
    conexao.close()
    return jsonify({"status": "sucesso", "mensagem": "Produto atualizado."})

@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
def remover_produto(produto_id):
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    conexao.commit()
    conexao.close()
    return jsonify({"status": "sucesso", "mensagem": "Produto removido."})

@app.route('/produtos', methods=['DELETE'])
def remover_todos_produtos():
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos")
    conexao.commit()
    conexao.close()
    return jsonify({"status": "sucesso", "mensagem": "Todos os produtos removidos."})
