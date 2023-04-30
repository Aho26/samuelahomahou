from django.db import models

# Create your models here.
class Message(models.Model):
    nom=models.CharField(max_length=200)
    mail=models.EmailField(max_length=200)
    sujet=models.CharField(max_length=255)
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.nom