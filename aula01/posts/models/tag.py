from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length=50)