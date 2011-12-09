from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms  # ModelForm

#from taggit.managers import TaggableManager

import datetime, os

class SBit(models.Model):
    '''A SBit is a SBitter message'''
    user        = models.ForeignKey('SBitter')
    msg         = models.CharField(max_length=140)
    pub_date    = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField()

    def __unicode__(self):
        return self.msg + ' (by ' + self.user.username + ')'


class SBitter(models.Model):
    '''A SBitter is a SBitter user'''
    user      = models.OneToOneField(User)
    followers = models.ManyToManyField("self", related_name='followees',
                                       symmetrical=False)

    created_at  = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.user.username
