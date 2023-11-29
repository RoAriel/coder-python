from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Post, Comentario, Usuario
from AppCoder.forms import UsuarioForm, BusquedaUsuarioForm

