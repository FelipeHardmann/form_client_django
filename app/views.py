'''
    Arquivo responsável por intermediar o front com o banco de dados
    recebendo usuários e fazendo suas regras de negócio.
'''

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Cliente

class ClienteCreateView(CreateView):
    '''
        Classe para criação da View
        Aqui criamos nossa visualização e comunicação para o front-end
    '''
    model = Cliente
    fields = '__all__'
    template_name = 'form_cliente.html'
    success_url = 'lista_clientes'
 

class ClienteListView(ListView):
    '''
        Classe para enviar informações de todos os clientes
        listando eles. 
    '''
    model = Cliente
    template_name = 'lista_clientes.html'


class ClienteDetailView(DetailView):
    '''
        Classe que vai detalhar somente um único cliente
    '''
    model = Cliente
    template_name = 'lista_cliente.html'
    context_object_name = 'cliente'


class ClienteUpdateView(UpdateView):
    '''
        Classe para atualizar dados de um cliente
    '''
    model = Cliente
    fields = '__all__'
    template_name = 'form_cliente.html'
    success_url = reverse_lazy('lista_clientes') 


class ClienteDeleteView(DeleteView):
    '''
        Classe para deletar clientes
    '''
    model = Cliente
    template_name = 'remover_cliente.html'
    success_url = reverse_lazy('lista_clientes') 
