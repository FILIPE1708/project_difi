from django.db import models
from .categoria import Categoria
from .tag import Tag

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=350)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, blank=True, null=True)
    tag = models.ManyToManyField(Tag)
