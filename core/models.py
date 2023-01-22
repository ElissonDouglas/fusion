from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = (f'{uuid.uuid4}.{ext}')
    return filename
    

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True
        

class Servicos(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),   
    )
    servicos = models.CharField('Serviço', max_length=100)
    descricao = models.CharField('Descricao', max_length=200)
    icone = models.CharField('icone', max_length=12, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        
    def __str__(self) -> str:
        return self.servicos
    

class Cargo(Base):
    cargo = models.CharField('cargo', max_length=100)
    
    class Meta:
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'
        
    def __str__(self) -> str:
        return self.cargo
    
    
class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        
    def __str__(self) -> str:
        return self.nome
    
    
class Recursos(Base):
    ICONE_CHOICES = (
        ('lni-laptop-phone', 'Laptop e Celular'),
        ('lni-leaf', 'Folha'),
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),   
    )
    
    COLUNAS = (
        ('coluna1', 'Coluna 1'),
        ('coluna2', 'Coluna 2'),
    )
    
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=17, choices=ICONE_CHOICES)
    coluna = models.CharField('Coluna', max_length=7,choices=COLUNAS, default='')
    
    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
        
    def __str__(self) -> str:
        return self.nome
