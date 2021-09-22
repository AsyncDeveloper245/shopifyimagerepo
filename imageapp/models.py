from django.db import models
from django.urls import reverse
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("image:home", args=[str(self.id)])
    

class Tag(models.Model):
    pass
#implement tag using the django_taggit module

