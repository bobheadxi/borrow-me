# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from .models import User
from .models import Item, Profile
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'password',
                    'items',
                    'user_karma',
                    'email',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'reputation')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'item_type',
                    'location',
                    'created_at',
                    'returned_at',
                    'user',
                    'karma',
                    'image',
                    'description',
                    'lat',
                    'lon',)


#admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Item, ItemAdmin)