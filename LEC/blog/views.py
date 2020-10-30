from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from .models import Post

# Create your views here.
def index(request):

    try:
        entradas = Post.objects.all()[:16]
    except:
        entradas = []
    
    context = {
        "entradas": entradas,
    }
    
    #return render(request,'GeneralTemplates/loginForm.html', {'form':form})
    return render(request,'blog/blog.html', context)

def post(request,id): #No manda el objeto en el contexto

    context={}
    print(id)

    try:
        post = Post.objects.get(Q(id = id))
    except:
        error = True
        context.update({'error': error})
        return render(request, 'blog/post.html', context)

    print(post.fecha_modificado)
    context.update({'post': post})
    return render(request, 'blog/post.html', context)

@permission_required('blog.can_publish', raise_exception=True)
def publish_post(request):
    return redirect(index)