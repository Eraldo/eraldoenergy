# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_original',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='original price'),
        ),
    ]
