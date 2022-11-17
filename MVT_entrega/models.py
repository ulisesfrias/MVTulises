from django.db import models

# Create your models here.

class familia(models.Model):

    nombres = models.CharField(max_length=50)
    edad = models.IntegerField()
