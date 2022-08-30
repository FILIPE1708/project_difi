from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from posts.models.categoria import Categoria
from rest_framework.decorators import api_view
from posts.serializer.categoria_serializer import CategoriaSerializer
from rest_framework.response import Response
from  rest_framework import status
from posts.models.tag import Tag

# Create your views here.

def listar_posts(request):
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias': categorias})

def listar_tags(request):
    tags = Tag.objects.all()
    return render(request, 'tag.html', {'tags': tags})

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'index.html'
    context_object_name = 'categorias'

@api_view(['GET', 'POST'])
def api_listar_categorias(request):
    if request.method  == 'GET':
        categorias = Categoria.objects.all()
        categoria_serializer = CategoriaSerializer(categorias, many=True)

        return Response(
            categoria_serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        Categoria.objects.create(
            nome = request.POST.get('nome')
        )

        return Response(status=status.HTTP_201_CREATED)



