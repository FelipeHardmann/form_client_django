'''
    Arquivo responsável por intermediar o front com o banco de dados
    recebendo usuários e fazendo suas regras de negócio.
'''

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from ..models import Cliente
from ..forms.cliente_forms import ClienteForm, EnderecoForm

class ClienteCreateView(CreateView):
    '''
        Classe para criação da View
        Aqui criamos nossa visualização e comunicação para o front-end
    '''
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form_cliente.html'
    success_url = 'lista_clientes'

    def get_context_data(self, **kwargs):
        '''
            Quando a view for chamada
            A função vai retornar qual contexto aparecerá na view
        '''
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context['form'] = ClienteForm
        context['endereco_form'] = EnderecoForm
        return context
    
    def post(self, request, *args, **kwargs):
        '''
            Função responsável por pegar os dados do formulário
            e se for válido, armazenar no banco
        '''
        cliente_form = ClienteForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse('lista_clientes')) 
 

class ClienteListView(ListView):
    '''
        Classe para enviar informações de todos os clientes
        listando eles. 
    '''
    model = Cliente
    template_name = 'clientes/lista_clientes.html'


class ClienteDetailView(DetailView):
    '''
        Classe que vai detalhar somente um único cliente
    '''
    model = Cliente
    template_name = 'clientes/lista_cliente.html'
    context_object_name = 'cliente'


class ClienteUpdateView(UpdateView):
    '''
        Classe para atualizar dados de um cliente
    '''
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form_cliente.html'
    success_url = reverse_lazy('lista_clientes') 

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        context['form'] = ClienteForm(instance=self.object)
        context['endereco_form'] = EnderecoForm(instance=self.object.endereco)
        return context
    
    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs['pk'])
        cliente_form = ClienteForm(data=request.POST or None, instance=cliente)
        endereco_form = EnderecoForm(data=request.POST or None, instance=cliente.endereco)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse('lista_clientes')) 


class ClienteDeleteView(DeleteView):
    '''
        Classe para deletar clientes
    '''
    model = Cliente
    template_name = 'clientes/remover_cliente.html'
    success_url = reverse_lazy('lista_clientes') 

    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs['pk'])
        cliente.endereco.delete()
        cliente.delete()
        return HttpResponseRedirect(reverse('lista_clientes'))
