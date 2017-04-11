# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:53:19 2017

@author: user
"""
from django.shortcuts import redirect, render

class ObjectCreateMixin:
    form_class = None
    template_name = ''
    def get(self, request):
        return render(request,
                      self.template_name,
                      {'form':self.form_class()})
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            render(request, self.template_name, {'form':bound_form})
