from django.contrib import admin
from .models import Cargo, Servicos, Funcionario, Recursos
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')
    

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'icone', 'ativo', 'modificado') 


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')   
    

@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone', 'coluna')

