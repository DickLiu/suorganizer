# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 12:58:56 2017

@author: user
"""
from django.views.generic import UpdateView as BaseUpdateView

class UpdateView(BaseUpdateView):
    template_name_suffix = '_form_update'
