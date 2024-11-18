from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Fornecedor, Produto, Cliente, Pedido
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Bem-vindo ao site!</h1><p>Use o menu para navegar.</p>")
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/listar_produtos.html', {'produtos': produtos})

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
    return render(request, 'core/criar_produto.html', {'categorias': categorias, 'fornecedores': fornecedores})

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
    return render(request, 'core/editar_produto.html', {'produto': produto, 'categorias': categorias, 'fornecedores': fornecedores})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')
