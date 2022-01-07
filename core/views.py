from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from django.views.generic import TemplateView
from .models import Representante, Pregao, Pregoeiro, Empresa, Secretaria, Secretario, Processo

from .forms import PregoeiroModelForm, ProcessoModelForm, EmpresaModelForm, PregaoModelForm, SecretariaModelForm, \
    SecretarioModelForm, RepresentanteModelForm
from django.urls import reverse_lazy


def index(request):
    context = {
        'processos':Processo.objects.all()
    }
    return render(request, 'index.html', context)


def pregoeiro(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = PregoeiroModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Pregoeiro salvo com sucesso!')
                form = PregoeiroModelForm()
            else:
                messages.error(request, 'Erro ao salvar Pregoeiro!')
        else:
            form = PregoeiroModelForm()
        context = {
            'form': form
        }
        return render(request, 'pregoeiro.html', context)
    else:
        return redirect('index')


def processo(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProcessoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Processo salvo com sucesso!')
                form = PregoeiroModelForm()
            else:
                messages.error(request, 'Erro ao salvar Processo!')
        else:
            form = ProcessoModelForm()
        context = {
            'form': form
        }
        return render(request, 'processo.html', context)
    else:
        return redirect('index')


def empresa(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = EmpresaModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empresa salvo com sucesso!')
                form = EmpresaModelForm()
            else:
                messages.error(request, 'Erro ao salvar Empresa!')
        else:
            form = EmpresaModelForm()
        context = {
            'form': form
        }
        return render(request, 'empresa.html', context)
    else:
        return redirect('index')


def pregao(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = PregaoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Pregão salvo com sucesso!')
                form = PregaoModelForm()
            else:
                messages.error(request, 'Erro ao salvar Empresa!')
        else:
            form = PregaoModelForm()
        context = {
            'form': form
        }
        return render(request, 'pregao.html', context)
    else:
        return redirect('index')


def secretaria(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = SecretariaModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empresa salvo com sucesso!')
                form = SecretariaModelForm()
            else:
                messages.error(request, 'Erro ao salvar Secretaria!')
        else:
            form = SecretariaModelForm()
        context = {
            'form': form
        }
        return render(request, 'secretaria.html', context)
    else:
        return redirect('index')


def secretario(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = SecretarioModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empresa salvo com sucesso!')
                form = SecretarioModelForm()
            else:
                messages.error(request, 'Erro ao salvar Secretário!')
        else:
            form = SecretarioModelForm()
        context = {
            'form': form
        }
        return render(request, 'secretario.html', context)
    else:
        return redirect('index')


def representante(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = RepresentanteModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Representante salvo com sucesso!')
                form = RepresentanteModelForm()
            else:
                messages.error(request, 'Erro ao salvar Representante!')
        else:
            form = RepresentanteModelForm()
        context = {
            'form': form
        }
        return render(request, 'representante.html', context)
    else:
        return redirect('index')



def list_pregoeiro(request):
    context = {
        'pregoeiros': Pregoeiro.objects.all()
    }
    return render(request, 'list_pregoeiro.html', context)


def list_pregao(request):
    context = {
        'pregoes': Pregao.objects.all()
    }
    return render(request, 'list_pregao.html', context)


def list_secretaria(request):
    context = {
        'secretarias': Secretaria.objects.all()
    }
    return render(request, 'list_secretaria.html', context)


def list_secretario(request):
    context = {
        'secretarios': Secretario.objects.all()
    }
    return render(request, 'list_secretario.html', context)


def list_representante(request):
    context = {
        'representantes': Representante.objects.all()
    }
    return render(request, 'list_representante.html', context)


def list_empresa(request):
    context = {
        'empresas': Empresa.objects.all()
    }
    return render(request, 'list_empresa.html', context)


def gerar_contrato(request):
    context ={

    }
    return render(request, 'gerar_contrato.html', context)


