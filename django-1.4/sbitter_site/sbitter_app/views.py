from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, \
    redirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt

from sbitter_app.models import *
from sbitter_app.model_forms import *
from sbitter_app.forms import *
from sbitter_app import helpers


def index(request):
    return render(request, "index.html", locals())


@login_required
def view_my_sbits(request):
    sbitter = Sbitter.objects.get(user=request.user)
    sbits = Sbit.objects.filter(sbitter=sbitter)
    greeting = helpers.simple_func()
    scraped_html = helpers.scrape('http://checkip.dyndns.org')
    return render(request, 'sbits_list.html', locals())


# def view_sbits(request, username):
#     sbitter = Sbitter.objects.get(user__username=username)
#     sbits = Sbit.objects.filter()


def search(request):
    form = SearchForm()
    return render(request, 'search.html', locals())
