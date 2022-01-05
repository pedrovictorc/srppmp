from django.contrib import admin

from .models import Representante, Pregao, Pregoeiro, Empresa, Secretaria, Secretario, Processo

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('cnpj','razao_social', 'modificado')


@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'modificado')


@admin.register(Pregoeiro)
class PregoeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'fone', 'modificado')


@admin.register(Pregao)
class PregaoAdmin(admin.ModelAdmin):
    list_display = ('pregao', 'ata', 'resumo', 'modificado')


@admin.register(Secretaria)
class SecretariaAdmin(admin.ModelAdmin):
    list_display = ('nome_secretaria', 'nome_fundo', 'modificado')


@admin.register(Secretario)
class SecretarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado')


@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('n_processo', 'n_pedido', 'modificado')

