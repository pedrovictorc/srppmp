from django.urls import reverse
from django.db import models


# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Empresa(Base):
    cnpj = models.CharField('CNPJ', unique=True, max_length=14)
    razao_social = models.CharField('Razão Social', max_length=50)
    cep = models.CharField('CEP', max_length=8)
    logradouro = models.CharField('Logradouro', max_length=100)
    complemento = models.CharField('Complemento', max_length=100)
    bairro = models.CharField('Bairro', max_length=50)
    numero = models.IntegerField('Número')
    estado = models.CharField('Estado', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    fone = models.CharField('Telefone', max_length=15)
    representante = models.ForeignKey('core.Representante', verbose_name='Representante', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razao_social


class Representante(Base):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField('Nome', max_length=50)
    comple_name = models.CharField('Solteiro e Brasileiro?', max_length=100)
    rg = models.CharField('RG', max_length=20, unique=True)
    cep = models.CharField('CEP', max_length=8)
    logradouro = models.CharField('Logradouro', max_length=100)
    complemento = models.CharField('Complemento', max_length=100)
    bairro = models.CharField('Bairro', max_length=50)
    numero = models.IntegerField('Número')
    estado = models.CharField('Estado', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    fone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'

    def __str__(self):
        return self.nome


class Pregoeiro(Base):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField('Nome', max_length=50)
    rg = models.CharField('RG', max_length=20, unique=True)
    fone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Pregoeiro'
        verbose_name_plural = 'Pregoeiros'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('pregoeiro-detail', kwargs={'pk': self.pk})


class Secretario(Base):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField('Secretário', max_length=50)
    rg = models.CharField('RG', max_length=20, unique=True)
    cargo = models.CharField('Cargo', max_length=50)
    fone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Secretário'
        verbose_name_plural = 'Secretarios'

    def __str__(self):
        return self.nome


class Secretaria(Base):
    sigla = models.CharField('Sigla', max_length=50)
    nome_secretaria = models.CharField('Secretaria', max_length=100)
    nome_fundo = models.CharField('Fundo', max_length=100)
    secretario = models.ForeignKey('core.Secretario', verbose_name='Secretario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Secretaria'
        verbose_name_plural = 'Secretarias'

    def __str__(self):
        return self.nome_secretaria


class Pregao(Base):
    pregao = models.CharField('Licitação', max_length=50)
    ata = models.CharField('Ata de Extrato Parcial', max_length=50)
    resumo = models.TextField('Resumo', max_length=500)
    objeto = models.TextField('Objeto da Licitação', max_length=500)
    dom = models.CharField('DOM', max_length=50)
    realinhamento = models.CharField('Realinhamento', max_length=50, blank=True)
    retificacao = models.CharField('Retificação', max_length=50, blank=True)
    homologacao = models.DateField('Homolocação')
    prazo = models.CharField('Prazo de Entrega', max_length=50)
    pregoeiro = models.ForeignKey('core.Pregoeiro', verbose_name='Pregoeiro', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pregão'
        verbose_name_plural = 'Pregões'

    def __str__(self):
        return self.pregao


class Processo(Base):
    n_contrato = models.CharField('Número do Contrato', max_length=15, unique=True)
    n_pedido = models.CharField('Número do Pedido', max_length=15, unique=True)
    n_processo = models.CharField('Número do Processo', max_length=15, unique=True)
    n_liberacao = models.CharField('Número do Liberação', max_length=15, unique=True)
    dt_protocolo = models.DateField('Data do Protocolo')
    pregao = models.ForeignKey('core.Pregao', verbose_name='Pregão', on_delete=models.CASCADE)
    dt_liberaca = models.DateField('Data da Liberação')
    EMPENHO = (
        ('ordinario', 'Ordinário'),
        ('global', 'Global'),
    )
    empenho = models.CharField('Empenho', max_length=10, choices=EMPENHO)
    secretaria = models.ForeignKey('core.Secretaria', verbose_name='Secretaria', on_delete=models.CASCADE)
    vigencia = models.CharField('Vigência', max_length=50)
    proj_atividade = models.CharField('Projeto Atividade', max_length=50)
    elemento_despesa = models.CharField('Elemento de Despesa', max_length=50)
    fonte_recurso = models.CharField('Fonte de Recurso', max_length=50)
    cod_aplicacao = models.CharField('Código de Aplicação', max_length=50)
    valor = models.FloatField('Valor')
    contratado = models.ForeignKey('core.Empresa', verbose_name='Empresa', on_delete=models.CASCADE)
    objeto = models.TextField('Objeto', max_length=500)
    justificativa = models.TextField('Justificativa', max_length=500)

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'

    def __str__(self):
        return self.n_processo
