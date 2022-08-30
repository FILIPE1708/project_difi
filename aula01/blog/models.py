from django.db import models

# Create your models here.

class TipoComentario(models.Model):
    tipo = models.CharField(max_length=50)

class Autor(models.Model):
    nome = models.CharField(max_length=50)

class Comentario(models.Model):
    descricao = models.CharField(max_length=200)
    likes = models.IntegerField()
    TipoComentario = models.ForeignKey(TipoComentario, on_delete=models.PROTECT, blank=True, null=True)
    Autor = models.ManyToManyField(Autor)


