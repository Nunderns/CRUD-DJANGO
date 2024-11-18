from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Fornecedor, Produto, Cliente, Pedido


# Página inicial
def index(request):
    return render(request, 'core/index.html')


# Produtos
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/Produtos/listar_produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        estoque = request.POST['estoque']
        categoria_id = request.POST['categoria']
        fornecedor_id = request.POST['fornecedor']
        categoria = Categoria.objects.get(id=categoria_id)
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, estoque=estoque, categoria=categoria, fornecedor=fornecedor)
        return redirect('listar_produtos')
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    return render(request, 'core/Produtos/criar_produto.html', {'categorias': categorias, 'fornecedores': fornecedores})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        produto.preco = request.POST['preco']
        produto.estoque = request.POST['estoque']
        produto.save()
        return redirect('listar_produtos')
    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()
    return render(request, 'core/Produtos/editar_produto.html', {'produto': produto, 'categorias': categorias, 'fornecedores': fornecedores})


def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')


# Categorias
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/listar_categorias.html', {'categorias': categorias})


def criar_categoria(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Categoria.objects.create(nome=nome)
        return redirect('listar_categorias')
    return render(request, 'core/criar_categoria.html')


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nome = request.POST['nome']
        categoria.save()
        return redirect('listar_categorias')
    return render(request, 'core/editar_categoria.html', {'categoria': categoria})


def deletar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listar_categorias')


# Fornecedores
def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'core/listar_fornecedores.html', {'fornecedores': fornecedores})


def criar_fornecedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        Fornecedor.objects.create(nome=nome, telefone=telefone, email=email)
        return redirect('listar_fornecedores')
    return render(request, 'core/criar_fornecedor.html')


def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        fornecedor.nome = request.POST['nome']
        fornecedor.telefone = request.POST['telefone']
        fornecedor.email = request.POST['email']
        fornecedor.save()
        return redirect('listar_fornecedores')
    return render(request, 'core/editar_fornecedor.html', {'fornecedor': fornecedor})


def deletar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    fornecedor.delete()
    return redirect('listar_fornecedores')


# Clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/Clientes/listar_clientes.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        Cliente.objects.create(nome=nome, email=email, telefone=telefone)
        return redirect('listar_clientes')
    return render(request, 'core/Clientes/criar_cliente.html')


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nome = request.POST['nome']
        cliente.email = request.POST['email']
        cliente.telefone = request.POST['telefone']
        cliente.save()
        return redirect('listar_clientes')
    return render(request, 'core/Clientes/editar_cliente.html', {'cliente': cliente})


def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('listar_clientes')


# Pedidos
def listar_pedidos(request):
    pedidos = Pedido.objects.select_related('cliente', 'produto').all()
    return render(request, 'core/Pedidos/listar_pedidos.html', {'pedidos': pedidos})


def criar_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        produto_id = request.POST['produto']
        quantidade = request.POST['quantidade']
        cliente = Cliente.objects.get(id=cliente_id)
        produto = Produto.objects.get(id=produto_id)
        Pedido.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)
        return redirect('listar_pedidos')
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'core/Pedidos/criar_pedido.html', {'clientes': clientes, 'produtos': produtos})


def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        produto_id = request.POST['produto']
        pedido.quantidade = request.POST['quantidade']
        pedido.cliente = Cliente.objects.get(id=cliente_id)
        pedido.produto = Produto.objects.get(id=produto_id)
        pedido.save()
        return redirect('listar_pedidos')
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'core/Pedidos/editar_pedido.html', {'pedido': pedido, 'clientes': clientes, 'produtos': produtos})


def deletar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('listar_pedidos')
