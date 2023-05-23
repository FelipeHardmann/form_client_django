from django.urls import include, path
from .views.cliente_views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDetailView, ClienteDeleteView
from .views.dependente_views import DependenteCreateView

urlpatterns = [
    path('form_cliente', ClienteCreateView.as_view(), name='cadastrar_cliente'),
    path('lista_clientes', ClienteListView.as_view(), name='lista_clientes'),
    path('form_cliente/<int:pk>', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('lista_cliente/<int:pk>', ClienteDetailView.as_view(), name='lista_cliente'),
    path('remover_cliente/<int:pk>', ClienteDeleteView.as_view(), name='remover_cliente'),
    path('form_dependente', DependenteCreateView.as_view(), name='cadastrar_dependente'),
]
