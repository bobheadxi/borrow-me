# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 12:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('return_at', models.DateTimeField()),
                ('returned_at', models.DateTimeField(blank=True, null=True)),
                ('karma', models.IntegerField()),
                ('image', models.TextField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=10)),
                ('lon', models.DecimalField(decimal_places=4, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('karma', models.IntegerField(default=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
