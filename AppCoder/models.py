from django.db import models

class Usuario(models.Model):
    id = models.IntegerField.auto_creation_counter
    nombre = models.CharField(max_length=40)

class Post(models.Model):
    id_post = models.IntegerField.auto_creation_counter
    post = models.CharField(max_length=150)

class Comentario(models.Model):
    id = models.IntegerField.auto_creation_counter
    id_post = models.IntegerField
    comentario = models.CharField(max_length=50)


