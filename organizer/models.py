from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31,unique=True,help_text='A label for URL config.')    
    def __str__(self):
        return self.name.title()        
    class Meta:
        ordering = ['name']        
    def get_absolute_url(self):
        return reverse('organizer_tag_detail', 
                       kwargs={'slug':self.slug})
    

class Startup(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(unique=True, help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)    
    def __str__(self):
        return self.name        
    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'
    def get_absolute_url(self):
        return reverse('organizer_startup_detail', kwargs={'slug':self.slug})

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published') #'date published'是verbose name
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)
    def __str__(self):
        return "{}:{}".format(self.startup, self.title)
    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date'] #只有ordering的作用，沒有getting的作用
        get_latest_by = 'pub_date' #只有getting的作用，沒有ordering的作用
    def get_absolute_url(self):
        return self.startup.get_absolute_url()
        

