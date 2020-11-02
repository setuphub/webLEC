from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.


def foro(request):

    context = {}
    categorias = Categoria.objects.all()

    context.update({'categorias': categorias})
    return render(request,'foro/categorias_foro.html',context)

def subcategoria(request,tCategoria,):

    context = {}
    subcategorias = Subcategoria.objects.get(Q(categoria = tCategoria))

    context.update({'subcategorias': subcategorias})

    return render(request,'foro/categorias_foro', context)