from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()
    

class Startup(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(unique=True, help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published') #'date published'是verbose name
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)

