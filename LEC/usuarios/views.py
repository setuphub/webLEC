from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import  formulario_registro, formulario_registro_equipo
# Create your views here.

def login(request):

    print(request.POST['nombre_usuario'])
    username = request.POST['nombre_usuario']
    password = request.POST['password']

    usuario = authenticate(request, username=username, password=password)
    print(usuario)

    if usuario is not None:
        login(request,usuario)
        return redirect('index')
    else:
        return redirect('index') 

def registro(request):
    """
    Funcion para realizar el registro de un usuario de manera manual(solo lo pueden hacer los jefes de equipo)
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = formulario_registro(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request,'blog/blog.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = formulario_registro()
    

    return render(request,'GeneralTemplates/registerForm.html', {'form':form})

def registro_equipo(request):
    """
    Funcion para registrar los datos del equipo
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = formulario_registro_equipo(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request,'blog/blog.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = formulario_registro_equipo()
    

    return render(request,'GeneralTemplates/teamRegister.html', {'form':form})
