'''
    Arquivo que será responsável pela criação das views
    de usuário, facilitará a segurança do programa
'''

from django.contrib.auth.models import User
from app.forms.usuario_forms import UsuarioForm
from django.views.generic import CreateView, ListView, DetailView
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