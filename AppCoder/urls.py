from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('postear/', crear_post),
    path('posts/', mostrar_posts),
    path('show/', show_html),

]