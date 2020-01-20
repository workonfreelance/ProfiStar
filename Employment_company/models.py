from django.db import models

# Create your models here.
class Form(models.Model):
    login = models.CharField(max_length = 25)
    Email = models.CharField(max_length = 25)
    file = models.FileField()

