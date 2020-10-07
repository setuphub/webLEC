from django import forms

class formulario_login(forms.Form):
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={'id':'username', 'type':'text', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Nombre de usuario')
    password = forms.CharField(widget=forms.TextInput(attrs={'id':'password', 'type':'password', 'class':'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}), label='Contraseña')
