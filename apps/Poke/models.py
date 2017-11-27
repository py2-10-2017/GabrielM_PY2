# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
import datetime
import re
regex_obj = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    pwd = forms.CharField(max_length=50, widget=forms.PasswordInput)
    dob = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.alias, self.email)

    

