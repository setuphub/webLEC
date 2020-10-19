from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from .forms import  formulario_registro, formulario_registro_equipo
# Create your views here.

def activation_sent_view(request):
    return render(request, 'usuarios/activacion_enviada.html')

def login(request):

    username = request.POST['nombre_usuario']
    password = request.POST['password']

    usuario = authenticate(request, username=username, password=password)
    print(usuario)

    if usuario is not None:
        do_login(request, usuario)
        return redirect('index')
    else:
        return redirect('index') 

def logout(request):
    do_logout(request)
    return redirect('index')



def registro(request):
    """
    Funcion para realizar el registro de un usuario de manera manual(solo lo pueden hacer los jefes de equipo)
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = formulario_registro(request.POST)
        print(form.errors)
        # check whether it's valid:
        if form.is_valid():
            print
            # process the data in form.cleaned_data as required
            user = form.save()
            user.refresh_from_db()

            user.is_active = False
            user.save()

            usuario = Usuario()
            usuario.user = user 
            usuario.save()

            current_site = get_current_site(request)

            subject = 'Activacion de cuenta'
            message = render_to_string('usuarios/activacion_cuenta.html',{
                'usuario' : user,
                'dominio' : current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            user.email_user(subject,message)
            return redirect('usuarios:activation_sent')

            # username = form.cleaned_data.get("username")
            # password = form.cleaned_data.get("password1")
            # usuario = authenticate(username=username, password=password)
            # print(usuario)

            # if usuario is not None:
            #     do_login(request, usuario)
            #     return redirect('index')
            # else:
            #     return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = formulario_registro()
    

    return render(request,'GeneralTemplates/registerForm.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.usuario.signup_confirmation = True
        user.save()
        do_login(request, user)
        return redirect('index')
    else:
        return render(request, 'activacion_error.html')

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
