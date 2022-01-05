from django import forms
from .models import Pregoeiro, Representante, Secretario, Processo, Empresa, Pregao, Secretaria


class PregoeiroModelForm(forms.ModelForm):
    class Meta:
        model = Pregoeiro
        fields = ['cpf', 'nome', 'rg', 'fone']


class RepresentanteModelForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = ['cpf', 'nome', 'comple_name', 'rg', 'cep', 'logradouro', 'complemento', 'bairro' ,'numero' ,'estado' ,'cidade' ,'fone']


class EmpresaModelForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['cnpj', 'razao_social', 'cep', 'logradouro', 'complemento', 'bairro', 'numero', 'estado', 'cidade', 'fone', 'representante']


class SecretarioModelForm(forms.ModelForm):
    class Meta:
        model = Secretario
        fields = ['cpf', 'nome', 'rg', 'cargo', 'fone']


class SecretariaModelForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = ['sigla', 'nome_secretaria', 'nome_fundo', 'secretario']


class ProcessoModelForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['n_contrato', 'n_pedido', 'n_processo', 'n_liberacao', 'dt_protocolo', 'pregao', 'dt_liberaca', 'empenho', 'secretaria', 'vigencia', 'proj_atividade', 'elemento_despesa', 'fonte_recurso', 'cod_aplicacao', 'valor', 'contratado', 'objeto', 'justificativa']


class PregaoModelForm(forms.ModelForm):
    class Meta:
        model = Pregao
        fields = ['pregao', 'ata', 'resumo', 'objeto', 'dom', 'realinhamento', 'retificacao', 'homologacao', 'prazo', 'pregoeiro']

