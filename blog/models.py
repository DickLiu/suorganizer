from django.db import models
from organizer.models import Startup, Tag

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField() #如不設定max_length，預設是50
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)
    
