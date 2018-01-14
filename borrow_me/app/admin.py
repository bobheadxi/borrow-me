# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from .models import User
from .models import Item, Profile
from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'karma',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'item_type',
                    'location',
                    'created_at',
                    'return_at',
                    'returned_at',
                    'user',
                    'karma',
                    'image',
                    'description',
                    'lat',
                    'lon',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Item, ItemAdmin)
