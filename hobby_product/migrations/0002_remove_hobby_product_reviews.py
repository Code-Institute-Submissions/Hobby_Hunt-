# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-14 15:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobby_product',
            name='reviews',
        ),
    ]