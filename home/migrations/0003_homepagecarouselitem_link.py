# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('home', '0002_homepagecarouselitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecarouselitem',
            name='link',
            field=models.ForeignKey(blank=True, related_name='+', null=True, to='wagtailcore.Page'),
        ),
    ]
