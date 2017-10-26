from datetime import date

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class TagManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class Tag(models.Model):
    name = models.CharField(max_length=31, verbose_name=_('name'))
    slug = models.SlugField(max_length=31,unique=True,help_text='A label for URL config.')    
    
    objects = TagManager()
    
    def __str__(self):
        return self.name.title()        
    class Meta:
        ordering = ['name']        
    def get_absolute_url(self):
        return reverse('organizer_tag_detail', 
                       kwargs={'slug':self.slug})
    def get_update_url(self):
        return reverse('organizer_tag_update',
                       kwargs={'slug':self.slug})
    def get_delete_url(self):
        return reverse('organizer_tag_delete',
                       kwargs={'slug':self.slug})        
    def published_posts(self):
        return self.blog_posts.filter(
                pub_date__lt=date.today())
        
    def natural_key(self):
        return (self.slug,)

class StartupManager(models.Manager):
    
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class Startup(models.Model):
    name = models.CharField(max_length=31, unique=True, verbose_name=_('name'))
    slug = models.SlugField(unique=True, help_text='A label for URL config.')
    description = models.TextField(verbose_name=_('description'))
    founded_date = models.DateField(verbose_name=_('date founded'))
    contact = models.EmailField(verbose_name=_('contact'))
    website = models.URLField(max_length=255, verbose_name=_('web site'))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_('tags'))    
    
    objects = StartupManager()
    
    def __str__(self):
        return self.name        
    
    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'
   
    def get_absolute_url(self):
        return reverse('organizer_startup_detail',
                       kwargs={'slug':self.slug})
    
    def get_update_url(self):
        return reverse('organizer_startup_update',
                       kwargs={'slug':self.slug})
    
    def get_delete_url(self):
        return reverse('organizer_startup_delete',
                kwargs={'slug':self.slug})
        
    def get_newslink_create_url(self):
        return reverse(
                'organizer_newslink_create',
                kwargs={'startup_slug': self.slug})
        
    def published_posts(self):
        return self.blog_posts.filter(
                pub_date__lt=date.today())
        
    def natural_key(self):
        return (self.slug,)

class NewsLinkManager(models.Manager):
    
    def get_by_natural_key(self, startup_slug, slug):
        return self.get(
                startup__slug=startup_slug,
                slug=slug)


class NewsLink(models.Model):
    title = models.CharField(max_length=63, verbose_name=_('title'))
    pub_date = models.DateField(verbose_name=_('date published')) #'date published'是verbose name
    link = models.URLField(max_length=255,verbose_name=_('link'))
    startup = models.ForeignKey(Startup)
    slug = models.SlugField(max_length=63)

    objects = NewsLinkManager()      
    
    def __str__(self):
        return "{}:{}".format(self.startup, self.title)
    
    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date'] #只有ordering的作用，沒有getting的作用
        get_latest_by = 'pub_date' #只有getting的作用，沒有ordering的作用
        unique_together = ('slug', 'startup')
    
    def get_absolute_url(self):
        return self.startup.get_absolute_url()
    
    def get_update_url(self):
        return reverse('organizer_newslink_update',
                       kwargs={
                               'startup_slug':self.startup.slug,
                               'newslink_slug': self.slug})
    
    def get_delete_url(self):
        return reverse('organizer_newslink_delete',
                       kwargs={
                               'startup_slug':self.startup.slug,
                               'newslink_slug': self.slug})
    
    def natural_key(self):
        return (
                self.startup.natural_key(),
                self.slug,)
        
    natural_key.dependencies = [
            'organizer.startup']

