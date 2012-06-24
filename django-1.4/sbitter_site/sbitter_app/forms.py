from django.contrib.auth.models import User
from django import forms
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from sbitter_app.models import *


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
