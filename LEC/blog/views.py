from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from .models import Entrada

# Create your views here.
def index(request):

    try:
        entradas = Entrada.objects.all()[:16]
    except:
        entradas = []
    
    context = {
        "entradas": entradas,
    }
    
    #return render(request,'GeneralTemplates/loginForm.html', {'form':form})
    return render(request,'blog/blog.html', context)

def entrada(request,id): #No manda el objeto en el contexto

    context={}
    print(id)

    try:
        entrada = Entrada.objects.get(Q(id = id))
    except:
        error = True
        context.update({'error': error})
        return render(request, 'blog/entrada.html', context)

    print(entrada.fecha_modificado)
    context.update({'entrada': entrada})
    return render(request, 'blog/entrada.html', context)

@permission_required('blog.can_publish', raise_exception=True)
def publish_post(request):
    return redirect(index)