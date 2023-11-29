from django import forms


class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()


class BusquedaUsuarioForm(forms.Form):
    nombre = forms.CharField()