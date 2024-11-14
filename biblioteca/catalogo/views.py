from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor
from .forms import AutorForm

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autor_list.html', {'autores': autores})

def novo_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'catalogo/autor_form.html', {'form': form})

def edita_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'catalogo/autor_form.html', {'form': form})

def deleta_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'catalogo/autor_confirm_delete.html', {'autor': autor})
