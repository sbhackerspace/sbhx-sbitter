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
    sbits = SBit.objects.all().order_by('-pub_date')
    return render(request, 'sbitter/sbit_list.html', {'sbits': sbits})

def logout_view(request):
    logout(request)
    messages.success(request, 'Come back soon!')
    return HttpResponseRedirect('/')


@login_required
def post_sbit(request, username):
    if username != request.user.username:
        HttpResponseRedirect('/') # Imposter!

    msg = forms.CharField().clean(request.POST['msg'])
    # return HttpResponse('msg == ' + msg)
    sbit = SBit(user=request.user, msg=msg)
    sbit.save()
    return HttpResponseRedirect('/' + username)


@login_required
def profile(request):
    sbits = SBit.objects.filter(user=request.user).order_by('-pub_date')
    return render(request, 'profile.html', {'sbits': sbits})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        newuser = User(username=forms.CharField().clean(request.POST['newuser']))
        newpassword = forms.CharField().clean(request.POST['newpassword'])
        #newuser = User(username=newuser)
        newuser.set_password(newpassword)
        newuser.save()
        return HttpResponseRedirect('/')

    else:
        return HttpResponseRedirect('/')

