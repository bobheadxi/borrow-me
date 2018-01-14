# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    item_type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    created_at = models.DateField()
    returned_at = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    karma = models.IntegerField()
    image = models.ImageField()
    description = models.CharField(max_length=50)
    lat = models.IntegerField()
    lon = models.IntegerField()


class User(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10)
    items = models.IntegerField()
    user_karma = models.IntegerField()
    email = models.CharField(max_length=20)