# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:59:05 2017
@author: user
"""
from django import forms
from .models import Post
from django.contrib.auth import get_user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
    
    def save(self, request, commit=True):
        post = super().save(commit=False)
        if not post.pk:
            post.author = get_user(request)
        if commit:
            post.save()
            self.save_m2m() 
            #這裡的self指的是form
            #save_m2m:
            #Save the many-to-many fields and generic relations for this form.
        return post
        
