from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms  # ModelForm

#from taggit.managers import TaggableManager

import datetime, os

class SBit(models.Model):
    user        = models.ForeignKey(User)
    msg         = models.CharField(max_length=140)
    pub_date    = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField()
