# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:36:39 2017

@author: user
"""
from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'blog'
    
    def ready(self):
        import blog.signals
