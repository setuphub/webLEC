from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from usuarios.forms import formulario_login

# Create your views here.
def index(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = formulario_login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request,'blog/blog.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = formulario_login()
    

    return render(request,'GeneralTemplates/loginForm.html', {'form':form})

@permission_required('blog.can_publish', raise_exception=True)
def publish_post(request):
    return redirect(index)