form django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/novo/', views.novo_autor, name='novo_autor'),
    path('autores/<int:pk>/editar/', views.edita_autor, name='edita_autor'),
    path('autores/<int:pk>/deletar/', views.deleta_autor, name='deleta_autor'),
]