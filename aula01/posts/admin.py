from django.contrib import admin
from posts.models.categoria import Categoria
from posts.models.tag import Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Categoria)

