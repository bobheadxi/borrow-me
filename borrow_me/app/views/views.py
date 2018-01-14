# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.models import Item, Profile
from django.contrib.auth.forms import UserCreationForm
import psycopg2
import utils

@login_required(login_url='/accounts/login')
def home(request):
    '''
    This is our homepage view. It displays a list of available and relevant items within 10km.
    '''
    # TODO : get location from request

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
            profile = Profile.objects.create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class ItemView(View):
    '''
    View for accessing and adding items!
    '''

    @method_decorator(login_required)
    def get(self, request):
        '''
        Get items
        '''
        items = Item.objects.all()
        context = {
            'items': items
        }

        # TODO: get location of user if available

        return render(request, 'site/item-detail.html', context)

    @method_decorator(login_required)
    def post(self, request):
        '''
        Add/modify item
        '''
        kwargs = dict(zip(request.POST.keys(), request.POST.values()))
        utils.cleanKwargsForItem(kwargs, request.user)
        i = Item(**kwargs)
        i.save()

        return render(request, 'index.html')

class UserView(View):
    '''
    Endpoint for users
    '''

    @method_decorator(login_required)
    def get(self, request):
        '''
        Retrieve and display data of user 
        '''
        # TODO
        context = {
            'user': request.user.profile
        }
        return render(request, 'index.html', context)
        
    @method_decorator(login_required)
    def post(self, request):
        '''
        Modify karma or requesting user
        '''
        kwargs = dict(zip(request.POST.keys(), request.POST.values()))
        karma = int(kwargs['karma_diff'])
        p = request.user.profile
        p.karma = p.karma + karma
        p.save()
        return render(request, 'index.html')
        