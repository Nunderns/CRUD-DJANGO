from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)

class Genero(models.Model):
    nome = models.CharField(max_length=50)

class Editora(models.Model):
    nome = models.CharField(max_length=100)

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    ano_publicacao = models.IntegerField()

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
