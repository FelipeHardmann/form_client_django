'''
    Arquivo que será responsável pela criação das views
    de usuário, facilitará a segurança do programa
'''

from typing import Optional
from app.models import User
from app.forms.usuario_forms import UsuarioForm, UsuarioUpdateForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminPermissionMixin


class UsuarioCreateView(AdminPermissionMixin, CreateView):
    '''
        Criando nosso usuário com autenticação
    '''
    model = User
    form_class = UsuarioForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('lista_usuarios')


class UsuarioListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/lista_usuarios.html'


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "usuarios/lista_usuario.html"
    context_object_name = "usuario"


class UsuarioUpdateView(AdminPermissionMixin, UpdateView):
    model = User
    form_class = UsuarioUpdateForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('lista_usuarios')

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuarios/remover_usuario.html'
    success_url = reverse_lazy('lista_usuarios')
    context_object_name = "usuario"

