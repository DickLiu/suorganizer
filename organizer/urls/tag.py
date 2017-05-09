
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:38:58 2017

@author: user
"""
from django.conf.urls import url
from ..views import (TagList, 
                     tag_detail, 
                     TagCreate,
                     TagUpdate,
                     TagDelete,
                     TagPageList)
                     
urlpatterns = [url(r'^$',
                  TagList.as_view(),
                  name='organizer_tag_list'),
              url(r'^(?P<page_number>\d+)/$',
                  TagPageList.as_view(),
                  name='organizer_tag_page'),
              url(r'^create/$',
                  TagCreate.as_view(),        
                  name='organizer_tag_create'),
              url(r'^(?P<slug>[\w\-]+)/$',
                  tag_detail,
                  name = 'organizer_tag_detail'),
              url(r'^(?P<slug>[\w\-]+)/update/$',
                  TagUpdate.as_view(),
                  name='organizer_tag_update'),
              url(r'^(?P<slug>[\w\-]+)/delete/$',
                  TagDelete.as_view(),
                  name='organizer_tag_delete'),]
