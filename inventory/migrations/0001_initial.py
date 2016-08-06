# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to='inventory/', verbose_name='image')),
                ('buyer', models.TextField(verbose_name='buyer')),
                ('price_min', models.IntegerField(blank=True, null=True, verbose_name='price minimum')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='price')),
                ('shipping', models.IntegerField(blank=True, null=True, verbose_name='shipping costs')),
                ('location', models.TextField(verbose_name='location')),
                ('notes', models.TextField(verbose_name='notes')),
                ('categories', models.ManyToManyField(to='inventory.Category', verbose_name='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='PortalLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, verbose_name='link')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item', verbose_name='item')),
                ('portal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Portal', verbose_name='portal')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='portals',
            field=models.ManyToManyField(through='inventory.PortalLink', to='inventory.Portal', verbose_name='portals'),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Status', verbose_name='status'),
        ),
    ]