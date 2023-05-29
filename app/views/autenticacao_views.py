from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    def get(self, request):
        data = {'form': AuthenticationForm}
        return render(request, 'autenticacao/login_usuario.html', data)

    def post(self, request):
        '''
            Vamos verificar o que o usuário digitou no campo username 
            e no campo password, esse campo é verificado pelo 
            método POST, que será reponsável pela validação 
            dor formulário
        '''
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)

        if usuario:
            login(request, usuario)
            return redirect('lista_usuarios')
        else:
            form_login = AuthenticationForm()
            return render(request, 'autenticacao/login_usuario.html', {
                'form': form_login, 'error': 'Usuário ou senha incorretos'
            })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('lista_usuarios')


class AlterarSenhaView(LoginRequiredMixin ,View):
    def get(self, request):
        data = {'form': PasswordChangeForm(request.user)}
        return render(request, 'autenticacao/alterar_senha.html', data)

    def post(self, request):
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('lista_usuarios')
        else:
            return render(request, 'autenticacao/alterar_senha.html', {'form': form_senha})