# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:03:08 2017

@author: user
"""
from django import forms
from .models import Tag #relative import
from django.core.exceptions import ValidationError

class TagForm(forms.Model):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
    def clean_name(self):
        return self.cleaned_data['name'].lower()
    def clean_slug(self):
        new_slug = self.clean_data['slug'].lower()
        if new_slug =='create':
            raise ValidationError('Slug may not be "create".')
            return new_slug
                           
    