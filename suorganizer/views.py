# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:49:13 2017

@author: user
"""
#from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def redirect_root(request):
    return redirect('blog_post_list')
