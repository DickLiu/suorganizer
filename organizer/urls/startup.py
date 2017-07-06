# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:39:24 2017

@author: user
"""
from django.conf.urls import url
from ..views import (StartupList,
                     StartupDetail,                    
                     StartupCreate,                    
                     StartupUpdate,                    
                     StartupDelete,)
                     
urlpatterns = [url(r'^create/$',        
                  StartupCreate.as_view(),        
                  name='organizer_startup_create'),    
              url(r'^$',        
                  StartupList.as_view(),        
                  name='organizer_startup_list'),
              url(r'^(?P<slug>[\w\-]+)/$',        
                  StartupDetail.as_view(),        
                  name='organizer_startup_detail'),    
              url(r'^(?P<slug>[\w\-]+)/update/$',        
                  StartupUpdate.as_view(),        
                  name='organizer_startup_update'),
              url(r'^(?P<slug>[\w\-]+)/delete/$',        
                  StartupDelete.as_view(),        
                  name='organizer_startup_delete'),]