import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    
    def setUp(self):
        self.file_name = f'{uuid.uuid4()}.png'
        
    def test_get_file_path(self):
        arquivo = get_file_path(None, "teste.png")
        self.assertTrue(len(arquivo), len(self.file_name))
    
    
class ServicosTestCase(TestCase):
    
    def setUp(self):
        self.servico = mommy.make("Servicos")
        
    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servicos)



class CargoTestCase(TestCase):
    
    def setUp(self):
        self.cargo = mommy.make("Cargo")
        
    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)
        
        
class FuncionarioTestCase(TestCase):
    
    def setUp(self):
        self.funcionario = mommy.make("Funcionario")
        
    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)
        

class RecursosTestCase(TestCase):
    
    def setUp(self):
        self.recurso = mommy.make("Recursos")
        
    def test_str(self):
        self.assertEquals(str(self.recurso), self.recurso.nome)
        
        