# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_homepagecarouselitem_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecarouselitem',
            name='link',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
