from django import forms


class PostForm(forms.Form):
    post = forms.CharField()


class BusquedaUsuarioForm(forms.Form):
    nombre = forms.CharField()