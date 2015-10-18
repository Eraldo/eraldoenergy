from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page


class HomePage(Page):
    slogan = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    box = RichTextField(blank=True)

    # class Meta:
    #     verbose_name = "Homepage"

    content_panels = Page.content_panels + [
        FieldPanel('slogan'),
        FieldPanel('body', classname="full", ),
        FieldPanel('box', classname="full", ),
        # InlinePanel('carousel_items')
    ]
