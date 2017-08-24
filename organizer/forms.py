# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:03:08 2017
@author: user
"""
from django import forms
from django.forms import ModelForm
from .models import Tag, NewsLink, Startup #relative import
from django.core.exceptions import ValidationError

class SlugCleanMixin:
    #Mixin class for slug cleaning method.
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()    
        if new_slug == 'create':        
            raise ValidationError('Slug may not be "create".')    
        return new_slug

class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
    def clean_name(self):
        return self.cleaned_data['name'].lower()
            
class NewsLinkForm(SlugCleanMixin, forms.ModelForm):

    class Meta:
        model = NewsLink
        exclude = ('startup',)

    def save(self, **kwargs):
        startup_obj = kwargs.get('startup_obj', None)
        if startup_obj is not None:
            instance = super.save(commit=False)
            instance.startup = startup_obj
            instance.save()
            self.save_m2m()
        else:
            instance  = super().save()
        return instance
        
class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        exclude = ('startup',)
            

    
                           
    