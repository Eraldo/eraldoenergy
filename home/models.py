from __future__ import unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class CarouselItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=100, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('link'),
    ]

    class Meta:
        abstract = True


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('HomePage', related_name='carousel_items')


class HomePage(Page):
    slogan = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    box = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('slogan'),
        FieldPanel('body', classname="full", ),
        FieldPanel('box', classname="full", ),
        InlinePanel('carousel_items', label="Carousel items"),
    ]
