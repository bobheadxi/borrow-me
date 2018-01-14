# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    if request.user.is_authenticated():
        return render(request, 'registration/profile.html')
    else:
        return HttpResponseRedirect('/accounts/login')