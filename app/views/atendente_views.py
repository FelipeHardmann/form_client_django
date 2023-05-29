from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.forms.atendente_forms import AtendenteForm
from app.models import Atendente


class AtendenteCreateView(LoginRequiredMixin ,CreateView):
    model = Atendente
    form_class = AtendenteForm
    template_name = "atendentes/form_atendente.html"
    success_url = "lista_atendentes"


class AtendenteListView(LoginRequiredMixin ,ListView):
    model = Atendente
    template_name = 'atendentes/lista_atendentes.html'
