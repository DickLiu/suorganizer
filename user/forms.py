# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:34:07 2017

@author: user
"""
import logging

from django.contrib.auth.forms import \
UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from .utils import ActivationMailFormMixin

logger = logging.getLogger(__name__)

class UserCreationForm(
        ActivationMailFormMixin,
        BaseUserCreationForm):
    
    mail_validation_error = (
            'User created. Could not send activation'
            'email. Please try again later.')
    
    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')
    
    def save(self, **kwargs):
        user = super().save(commit=False)
        if not user.pk:
            user.is_active = False
            send_mail = True
        else:
            send_mail = False
        user.save()
        self.save_m2m()
        if send_mail:
            self.send_mail(user=user, **kwargs)
        return user
    
class ResendActivationEmailForm(
        ActivationMailFormMixin, forms.Form):
    email = forms.EmailField()
  
    mail_validation_error = (
          'Could not re-send activation email.'
          'please try again later.')
    def save(self, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(
                    email=self.cleaned_data['email'])
        except:
            logger.warning(
                  'Resend Activation: No user with'
                  'email: {}.'.format(
                          self.cleaned_data['email']))
            return None
        self.send_mail(user=user, **kwargs)
        return user
        
  