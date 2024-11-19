from django.shortcuts import render, redirect
from django.contrib import messages

def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        preco = request.POST.get('preco', '').strip()
        estoque = request.POST.get('estoque', '').strip()
        categoria = request.POST.get('categoria', '').strip()
        fornecedor = request.POST.get('fornecedor', '').strip()

        if not nome or not descricao or not preco or not estoque or not categoria or not fornecedor:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'criar_produto.html')

        try:
            preco = float(preco)
            estoque = int(estoque)
            if preco <= 0 or estoque < 0:
                raise ValueError()
        except ValueError:
            messages.error(request, "Preço deve ser um número positivo e estoque deve ser um número inteiro positivo ou zero.")
            return render(request, 'criar_produto.html')


        messages.success(request, "Produto criado com sucesso!")
        return redirect('listar_produtos')

    return render(request, 'criar_produto.html')
