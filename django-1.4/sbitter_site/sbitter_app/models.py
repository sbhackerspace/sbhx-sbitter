from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms  # ModelForm

from tagging.fields import TagField

import datetime
import os


class Base(models.Model):
    created_at  = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        abstract = True


class Sbitter(Base):
    user = models.ForeignKey(User, unique=True)
    # followers = models.ManyToManyField("self", symmetric=False)


class Sbit(Base):
    sbitter = models.ForeignKey(Sbitter)
    message = models.CharField(max_length=140)

    def say_message(self):
        print self.sbitter.user.username + " had this to say: " + self.message
