import requests

base_url = "http://localhost:5000"

def criar_produto():
    new_product = {"nome": "Produto Exemplo", "descricao": "Este é um produto de exemplo.", "preco": 9.99}
    response = requests.post(f"{base_url}/produtos", json=new_product)
    print("POST /produtos:", response.json())

def buscar_produtos():
    response = requests.get(f"{base_url}/produtos")
    print("GET /produtos:", response.json())
"""
def buscar_produto(produto_id):
    response = requests.get(f"{base_url}/produtos/{produto_id}")
    print(f"GET /produtos/{produto_id}:", response.json())

def atualizar_produto(produto_id):
    updated_product = {"nome": "Produto Exemplo Atualizado", "descricao": "Este é um produto de exemplo atualizado.", "preco": 12.99}
    response = requests.put(f"{base_url}/produtos/{produto_id}", json=updated_product)
    print(f"PUT /produtos/{produto_id}:", response.json())

def remover_produto(produto_id):
    response = requests.delete(f"{base_url}/produtos/{produto_id}")
    print(f"DELETE /produtos/{produto_id}:", response.json())

def remover_todos_produtos():
    response = requests.delete(f"{base_url}/produtos")
    print("DELETE /produtos:", response.json())
"""
if __name__ == "__main__":
    criar_produto()
    buscar_produtos()
    """ buscar_produto(1)
    atualizar_produto(1)
    remover_produto(1)
    remover_todos_produtos()
    """
