# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 16:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_item_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='borrowed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='borrowed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_borrowed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
