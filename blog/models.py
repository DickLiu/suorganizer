from django.db import models
from organizer.models import Startup, Tag
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date') #如不設定max_length，預設是50
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')    
    def __str__(self):
        return "{}:{}".format(self.title, self.pub_date.strftime('%Y-%m-%d')) #將時間用客製化格式顯示的函數strftime()        
    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
    def get_absolute_url(self):
        return reverse('blog_post_detail', 
                       kwargs={'year':self.pub_date.year, 
                       'month':self.pub_date.month,        
                       'slug':self.slug} )
        
    
