from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import User


class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'cargo')


class UsuarioUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
