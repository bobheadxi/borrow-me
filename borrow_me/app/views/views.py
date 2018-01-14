# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from borrow_me.app.models import Item
from django.contrib.auth.forms import UserCreationForm
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

def signup(request):
    '''
    Signup stuff.
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class ItemView(View):
    '''
    View for accessing and adding items!
    '''

    def get(self, request):
        '''
        Get items
        '''
        items = Item.objects.get()
        context = {
            items: items
        }

        # TODO: get location of user if available

        return render(request, 'index.html', context)

    def post(self, request):
        '''
        Add item
        '''
        kwargs = dict(request.POST)
        i = Item(**kwargs)
        i.save()

        return render(request, 'index.html')

    def put(self, request):
        '''
        Modify item
        '''
        kwargs = dict(request.PUT)
        i = Item(**kwargs)
        i.save()

        return render(request, 'index.html')
