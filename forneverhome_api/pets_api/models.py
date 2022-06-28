from django.db import models

# Create your models here.
class Pets(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=32)
    image = models.URLField(max_length=500)
    owner = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    thoughts = models.CharField(max_length=50)
