'''
    Arquivo que será responsável pela criação das views
    de usuário, facilitará a segurança do programa
'''

from django.contrib.auth.models import User
from app.forms.usuario_forms import UsuarioForm, UsuarioUpdateForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class UsuarioCreateView(CreateView):
    '''
        Criando nosso usuário com autenticação
    '''
    model = User
    form_class = UsuarioForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('lista_usuarios')


class UsuarioListView(ListView):
    model = User
    template_name = 'usuarios/lista_usuarios.html'


class UsuarioDetailView(DetailView):
    model = User
    template_name = "usuarios/lista_usuario.html"
    context_object_name = "usuario"


class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UsuarioUpdateForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('lista_usuarios')


class UsuarioDeleteView(DeleteView):
    model = User
    template_name = 'usuarios/remover_usuario.html'
    success_url = reverse_lazy('lista_usuarios')
    context_object_name = "usuario"

