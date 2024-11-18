from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    # Produtos
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/<int:id>/editar/', views.editar_produto, name='editar_produto'),
    path('produtos/<int:id>/deletar/', views.deletar_produto, name='deletar_produto'),

    # Categorias
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/novo/', views.criar_categoria, name='criar_categoria'),
    path('categorias/<int:id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:id>/deletar/', views.deletar_categoria, name='deletar_categoria'),

    # Fornecedores
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/novo/', views.criar_fornecedor, name='criar_fornecedor'),
    path('fornecedores/<int:id>/editar/', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedores/<int:id>/deletar/', views.deletar_fornecedor, name='deletar_fornecedor'),

    # Clientes
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/novo/', views.criar_cliente, name='criar_cliente'),
    path('clientes/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:id>/deletar/', views.deletar_cliente, name='deletar_cliente'),

    # Pedidos
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/novo/', views.criar_pedido, name='criar_pedido'),
    path('pedidos/<int:id>/editar/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/<int:id>/deletar/', views.deletar_pedido, name='deletar_pedido'),
]
