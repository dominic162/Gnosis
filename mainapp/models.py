from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    slug=models.SlugField()
    userimage=models.ImageField(upload_to="userimage/",default='default_profile.jpg')
    interest=TaggableManager()

    def __str__(self):
        return self.name