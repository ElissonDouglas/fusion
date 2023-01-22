from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    
    def setUp(self):
        self.dados = {
            "nome": 'elisson douglas',
            'email': 'elisson@gmail.com',
            'assunto': 'meu assunto123',
            'mensagem': 'minha mensagem 123'
        }
        
        self.cliente = Client()
        
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
        
    def test_form_invalid(self):
        dados = {
            'nome': 'Elisson',
            'assunto': 'eli@gmail.com'
        }
        
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
    