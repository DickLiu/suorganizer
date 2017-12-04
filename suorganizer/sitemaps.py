# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:52:56 2017

@author: user
"""
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


from blog.sitemaps import (
        PostSitemap, PostArchiveSitemap)
from organizer.sitemaps import (
        TagSitemap, StartupSitemap)

class RootSitemap(Sitemap):
    priority = 0.6
    
    def items(self):
        return [
                'about_site',
                'blog_post_list',
                'contact',
                'dj_auth:login',
                'organizer_startup_list',
                'organizer_tag_list',
                ]
    def location(self, url_name):
        return reverse(url_name)
    

sitemaps = {
    'posts': PostSitemap,
    'startups': StartupSitemap,
    'tags': TagSitemap,
    'post-archives': PostArchiveSitemap,
    'roots': RootSitemap,
}