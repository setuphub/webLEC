from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formulario_login(forms.Form):
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={'id':'username', 'name':'username', 'type':'text', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Nombre de usuario')
    password = forms.CharField(widget=forms.TextInput(attrs={'id':'password', 'name':'passwd', 'type':'password', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Contraseña')


class formulario_registro(UserCreationForm):
    """formulario_registro definition."""

    # TODO: Define form fields here

    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'name', 'name':'name', 'type':'text', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Nombre')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'surname', 'name':'surname', 'type':'text', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Apellidos')
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'username', 'name':'username', 'type':'text', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='id PSN') #id_psn
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email', 'name':'email', 'type':'email', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='email')
    password1 = forms.CharField(widget=forms.TextInput(attrs={'id':'password', 'name':'passwd', 'type':'password', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Contraseña')
    password2 = forms.CharField(widget=forms.TextInput(attrs={'id':'password2', 'name':'passwd2', 'type':'password', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Repetir contraseña')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2' )

class formulario_registro_equipo(forms.Form):
    """formulario_registro_equipo definition."""

    # TODO: Define form fields here
    nombreEquipo = forms.CharField(widget=forms.TextInput(attrs={'id':'nombreEquipo', 'name':'nombreEquipo', 'onKeyup':'checkform()', 'type':'text', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Nombre de equipo')
    abreviatura = forms.CharField(widget=forms.TextInput(attrs={'id':'abreviatura', 'name':'abreviatura', 'type':'text', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Abreviatura')
    localizacion = forms.CharField(widget=forms.TextInput(attrs={'id':'localizacion', 'name':'localizacion', 'type':'text', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Localizacion')
    emailEquipo = forms.CharField(widget=forms.TextInput(attrs={'id':'emailEquipo', 'name':'emailEquipo', 'type':'email', 'onKeyup':'checkform()', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='email de equipo')
    id_piloto = forms.CharField(widget=forms.TextInput(attrs={'id':'id_piloto0', 'name':'id_piloto0', 'type':'text', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Piloto')
    email_piloto = forms.EmailField(widget=forms.TextInput(attrs={'id':'email_piloto0', 'name':'email_piloto0', 'type':'email', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Piloto')


