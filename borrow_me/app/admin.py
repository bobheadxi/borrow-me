# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User, Item

class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'password',
                    'items',
                    'user_karma',
                    'email',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_type',
                    'location',
                    'created_at',
                    'returned_at',
                    'user',
                    'karma',
                    'image',
                    'description',
                    'lat',
                    'lon',)


admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)