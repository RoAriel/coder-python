from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Post, Comentario, Usuario
from AppCoder.forms import PostForm, BusquedaUsuarioForm


def mostrar_posts(request):
    posts = Post.objects.all()
    contexto = {
        "posts": posts,
    }
    return render(request, "AppCoder/posts.html", contexto)

def crear_post(request):
    if request.method == "POST":
        # Crear curso
        post_formulario = PostForm(request.POST)
        if post_formulario.is_valid():
            informacion = post_formulario.cleaned_data
            post_crear = Post(post=informacion["post"])
            post_crear.save()
            return redirect("/app/posts/")

    post_formulario = PostForm()
    contexto = {
        "form": post_formulario
    }
    return render(request, "AppCoder/crear_post.html", contexto)

def show_html(request):
    post = Post.objects.first()
    contexto = {"post": post,}
    return render(request, 'index.html', contexto)