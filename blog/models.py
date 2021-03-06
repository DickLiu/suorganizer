from datetime import date

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from organizer.models import Startup, Tag

class PostQueryset(models.QuerySet):
    
    def published(self):
        return self.filter(
                pub_date__lte=date.today())

class BasePostManager(models.Manager):
    
    def get_queryset(self):
        return (
                PostQueryset(
                        self.model,
                        using=self._db,
                        hints=self._hints)
                .select_related('author__profile'))
    
    
    def get_by_natural_key(
            self, pub_date, slug):
        return self.get(
                pub_date=pub_date,
                slug=slug)
        
PostManager = BasePostManager.from_queryset(
        PostQueryset)

class Post(models.Model):
    title = models.CharField(max_length=63, verbose_name=_('title'))
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date',
                            verbose_name=_('slug')) #如不設定max_length，預設是50
    text = models.TextField(verbose_name=_('text'))
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True, verbose_name=_('tags'))
    startups = models.ManyToManyField(Startup, related_name='blog_posts', blank=True, verbose_name=_('startups'))
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name='blog_posts')
    
    objects = PostManager()
    
    def __str__(self):
        return "{}:{}".format(self.title, self.pub_date.strftime('%Y-%m-%d')) #將時間用客製化格式顯示的函數strftime()        
    class Meta:
        verbose_name = _('blog post')
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
        permissions= (
                ('view_future_post',
                 'Can view unpublished Post'),
        )
        index_together = (
                ('slug', 'pub_date'),)
    def get_absolute_url(self):
        return reverse('blog_post_detail', 
                       kwargs={'year':self.pub_date.year, 
                       'month':self.pub_date.month,        
                       'slug':self.slug} )
    def get_update_url(self):
        return reverse('blog_post_update',
                kwargs={'year':self.pub_date.year,
                        'month':self.pub_date.month,
                        'slug':self.slug})
    def get_delete_url(self):
        return reverse('blog_post_delete',
                kwargs={'year':self.pub_date.year,
                        'month':self.pub_date.month,
                        'slug':self.slug})
    def get_archive_year_url(self):
        return reverse(
                'blog_post_archive_year',
                kwargs={'year':self.pub_date.year})
    def get_archive_month_url(self):
        return reverse(
                'blog_post_archive_month',
                kwargs={'year':self.pub_date.year,
                        'month':self.pub_date.month})
    
    def natural_key(self):
        return(
                self.pub_date,
                self.slug,)
    natural_key.dependencies = [
            'organizer.startup',
            'organizer.tag',
            'user.user',
            ]
    
    def formatted_title(self):
        return self.title.title()
    
    def short_text(self):
        if len(self.text) > 20:
            short = ' '.join(self.text.split()[:20])
            short += ' ...'
        else:
            short = self.text
        return short
            

    