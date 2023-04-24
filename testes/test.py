import sys
sys.path.append('C:/Users/Rodrigo/Desktop/votacao')

import unittest
import json
from app.rotas import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        new_product = {"nome": "Produto Exemplo", "descricao": "Este é um produto de exemplo.", "preco": 9.99}
        response = self.app.post('/produtos', data=json.dumps(new_product), content_type='application/json')
        self.created_product_id = json.loads(response.data)["id"]

    def test_criar_produto(self):
        new_product = {"nome": "Produto Exemplo", "descricao": "Este é um produto de exemplo.", "preco": 9.99}
        response = self.app.post('/produtos', data=json.dumps(new_product), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_buscar_produtos(self):
        response = self.app.get('/produtos')
        self.assertEqual(response.status_code, 200)
""" 
    def test_buscar_produto(self):
        response = self.app.get(f'/produtos/{self.created_product_id}')
        self.assertEqual(response.status_code, 200)

    def test_atualizar_produto(self):
        updated_product = {"nome": "Produto Exemplo Atualizado", "descricao": "Este é um produto de exemplo atualizado.", "preco": 12.99}
        response = self.app.put('/produtos/1', data=json.dumps(updated_product), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_remover_produto(self):
        response = self.app.delete('/produtos/1')
        self.assertEqual(response.status_code, 200)
 """
""" def test_remover_todos_produtos(self):
        response = self.app.delete('/produtos')
        self.assertEqual(response.status_code, 200) """

if __name__ == '__main__':
    unittest.main()
