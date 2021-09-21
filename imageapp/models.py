from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)

class Tag(models.Model):
    pass
#implement tag using the django_taggit module

