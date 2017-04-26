# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:54:05 2017

@author: user
"""
from django.conf.urls import url
from .views import ContactView

urlpatterns = [url(r'^$',
                   ContactView.as_view(),
                   name='contact'),]
