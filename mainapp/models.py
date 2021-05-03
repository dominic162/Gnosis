from django.db import models
from taggit.managers import TaggableManager
from phone_field import PhoneField

# Create your models here.

class appuser(models.Model):
    username    = models.CharField(max_length=15)
    name        = models.CharField(max_length=15)
    email       = models.EmailField()
    slug        = models.SlugField()
    userimage   = models.ImageField(upload_to = "userimage/",default='default_profile.jpg')
    tags        = TaggableManager()

    def __str__(self):
        return self.name

class doubts(models.Model):
    question    = models.CharField(max_length = 200)
    author      = models.ForeignKey('appuser', on_delete = models.CASCADE)
    tags        = TaggableManager()

    def __str__(self):
        return self.question

class solution(models.Model):
    answer      = models.TextField()
    question    = models.ForeignKey('doubts', on_delete = models.CASCADE)
    author      = models.ForeignKey('appuser', on_delete = models.CASCADE)

    def __str__(self):
        return self.answer

class book(models.Model):
    name        = models.CharField(max_length = 200)
    author      = models.CharField( max_length = 100 )
    uploaded_by = models.ForeignKey( 'appuser' , on_delete = models.CASCADE)
    thumbnail   = models.ImageField(upload_to = "thumbnail/" , default = 'default_thumbnail.jpg')
    bookpdf     = models.FileField(upload_to= "book/")
    no_of_pages = models.IntegerField()
    tags        = TaggableManager()

    def __str__(self):
        return self.name

class contact(models.Model):
    name        = models.CharField(max_length = 50)
    email       = models.EmailField()
    phone       = PhoneField(blank = True)
    message     = models.TextField()

    def __str__(self):
        return self.name

class extra_info(models.Model):
    bio         = models.CharField( blank = True , max_length  = 100 )
    site_link   = models.URLField(  blank       = True )
    gthb_link   = models.URLField(  blank       = True )
    twtr_link   = models.URLField(  blank       = True )
    inst_link   = models.URLField(  blank       = True )
    fb_link     = models.URLField(  blank       = True )
    author      = models.ForeignKey('appuser' , on_delete= models.CASCADE)

    def __str__(self):
        return self.author.name

class reviews( models.Model ):
    name = models.CharField( max_length = 20 )
    review = models.TextField()

    def __str__(self):
        return self.name