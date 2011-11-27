from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.core import serializers
#from django.core.context_processors import csrf
#from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import loader, RequestContext
#from django.views.decorators.csrf import csrf_exempt

from sbhx_sbitter.sbitter.models import *

@login_required
def index(request):
    sbits = SBit.objects.filter(user=request.user).order_by('-pub_date')
    return render(request, 'sbitter/sbit_list.html', {'sbits': sbits})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = forms.CharField().clean(request.POST['username'])
        password = forms.CharField().clean(request.POST['password'])

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Wrong username or password')
            return HttpResponseRedirect('/')
            
    else:
        return HttpResponseRedirect('/')
    

def logout_view(request):
    logout(request)
    messages.success(request, 'Come back soon!')
    return HttpResponseRedirect('/')

def userspage(request, username):    
    sbits = SBit.objects.filter(user__username=username).order_by('-pub_date')
    return render(request, 'users.html', {'sbits': sbits})


@login_required
def post_userspage(request, username): 
    users_sbit = forms.CharField().clean(request.POST['users_sbit'])
    return HttpResponse(users_sbit)
    sbit = SBit(user=request.user, msg=users_sbit)
    sbit.save()
    return HttpResponseRedirect('/' + username)

