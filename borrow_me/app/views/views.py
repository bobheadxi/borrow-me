# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from app.models import Item
import psycopg2
import utils

# request.user is the username
@login_required(login_url='/accounts/login')
def home(request):
    '''
    This is our homepage view. It displays a list of available and relevant items within 10km.
    '''
    # TODO : get location from request

    return render(request, 'index.html')

def additem(request):
    '''
    This creates a new item.
    '''
    i = Item()
    i.save()

    return render(request, 'index.html')