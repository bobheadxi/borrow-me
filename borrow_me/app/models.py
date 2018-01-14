# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    item_type = models.CharField(max_length=30, blank = False)
    location = models.CharField(max_length=30, blank = False)
    created_at = models.DateTimeField(auto_now_add = True, blank = False, editable = False)
    returned_at = models.DateTimeField(blank = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = False)
    karma = models.IntegerField(blank = False)
    image = models.TextField(max_length=50,blank = False)
    description = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits = 10, decimal_places = 4, blank = False)
    lon = models.DecimalField(max_digits = 10, decimal_places = 4,blank = False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(blank=False, default=10)



# class User(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     password = models.CharField(max_length=10)
#     items = models.IntegerField()
#     user_karma = models.IntegerField()
#     email = models.CharField(max_length=20)