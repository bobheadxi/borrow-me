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
from app.forms import UserCreateForm
from datetime import datetime
import psycopg2
import utils

@login_required(login_url='/accounts/login')
def home(request):
    '''
    This is our homepage view. It displays a list of available and relevant items within 10km.
    '''
    # TODO : get location from request

    return redirect('item')

def signup(request):
    '''
    Signup stuff.
    '''
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile.objects.create(user=user)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/accounts/login')
def profile(request):
    context = {
        'user' : request.user,
        'borrowing' : Item.objects.filter(available = False, borrowed_by = request.user),
        'lending' : Item.objects.filter(user = request.user)
    }

    return render(request, 'registration/profile.html', context)

class ItemView(View):
    '''
    View for accessing and adding items!
    '''

    @method_decorator(login_required)
    def get(self, request):
        '''
        Get items
        Optionally takes lon, lat params
        '''
        kwargs = dict(zip(request.GET.keys(), request.GET.values()))
        items = Item.objects.filter(available=True)

        lon = kwargs.get('lon', None)
        lat = kwargs.get('lat', None)
        if lon and lat:
            ignore = []
            for i in items:
                item_coord = (i.lon, i.lat)
                user_coord = (lon, lat)
                if utils.distance(item_coord, user_coord) == -1:
                    ignore.append(i.id)
            items.exclude(id__in=ignore)

        context = {
            'karma': request.user.profile.karma,
            'items': items
        }

        return render(request, 'site/item-detail.html', context)

    @method_decorator(login_required)
    def post(self, request):
        '''
        Add/modify item ((submit))
        '''
        kwargs = dict(zip(request.POST.keys(), request.POST.values()))
        if kwargs.get('available', None) is not None:
            p = request.user.profile
            i = Item.objects.get(id=kwargs['id'])
            # Logic for borrowing
            if kwargs['available'] == 'True':
                if p.karma < i.karma:
                    # TODO : error message
                    context = {
                        'karma': request.user.profile.karma,
                        'items': Item.objects.filter(available=True),
                        'errorMsg': 'Not enough karma'
                    }
                    return render(request, 'site/item-detail.html', context)
                p.karma -= i.karma
                p.save()
                i.available = False
                i.borrowed_by = request.user
                i.borrowed_at = datetime.now()
                i.save()
                i.user.profile.karma += 5
                i.user.profile.save()
                utils.sendLoanedEmail(i.user.email, i.item_type, request.user)
                utils.sendLoanerEmail(request.user.email, i.item_type, i.return_at)
            # Logic for returning amnd deleting
            else:
                if request.user == i.user:
                    i.delete()
                else:
                    i.returned_at = datetime.now()
                    i.borrowed_by = None
                    i.save()
                    utils.sendReturnedEmail(i.user.email, i.item.type, request.user)

        else:
            utils.cleanKwargsForItem(kwargs, request.user)
            i = Item(**kwargs)
            i.save()

        return redirect('item')

# TODO : Deprecate?
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
        return redirect('item')
        # return render(request, 'index.html')
