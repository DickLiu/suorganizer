# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:53:26 2017

@author: user
"""
from django.conf.urls import url
from .views import (PostList, post_detail,
                    PostCreate, PostUpdate,
                    PostDelete)

urlpatterns=[url(r'^create/$',
                 PostCreate.as_view(),
                 name='blog_post_create'),
             url(r'^$', 
                 PostList.as_view(),
                 name='blog_post_list'),
             url(r'^(?P<year>\d{4})/'             
                 r'(?P<month>\d{1,2})/'             
                 r'(?P<slug>[\w\-]+)/$', 
                post_detail, 
                name='blog_post_detail'),
             url(r'^(?P<year>\d{4})/'             
                 r'(?P<month>\d{1,2})/'             
                 r'(?P<slug>[\w\-]+)/'
                 r'update/$',
                 PostUpdate.as_view(),
                 name='blog_post_update'),
             url(r'^(?P<year>\d{4})/'             
                 r'(?P<month>\d{1,2})/'             
                 r'(?P<slug>[\w\-]+)/'
                 r'delete/$',
                 PostDelete.as_view(),
                 name='blog_post_delete'),]
                

