from django.db import models

class Usuario(models.Model):
    id = models.IntegerField.auto_creation_counter
    nombre = models.CharField(max_length=40)
    mail = models.EmailField

    def __str__(self):
        return f"Usuario: {self.nombre}, Mail: {self.mail}"

class Post(models.Model):
    id_post = models.IntegerField.auto_creation_counter
    post = models.CharField(max_length=150)

    def __str__(self):
        return f"POST: {self.post}"

class Comentario(models.Model):
    id = models.IntegerField.auto_creation_counter
    id_post = models.IntegerField
    comentario = models.CharField(max_length=50)

    def __str__(self):
        return f"Post_id: {self.id_post}, comentario: {self.comentario}"


