from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


class Status(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')

    def __str__(self):
        return self.name


class Quality(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _('quality')
        verbose_name_plural = _('qualities')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class Portal(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class PortalLink(models.Model):
    portal = models.ForeignKey(
        verbose_name=_('portal'),
        to='Portal',
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        verbose_name=_('item'),
        to='Item',
        on_delete=models.CASCADE,
    )
    link = models.URLField(
        verbose_name=_('link'),
        blank=True,
    )

    def __str__(self):
        return self.portal


def image_path(instance, filename):
    pass


class Item(models.Model):
    name = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
    )
    link = models.URLField(
        verbose_name=_('link'),
        blank=True,
        max_length=1000,
    )
    status = models.ForeignKey(
        verbose_name=_('status'),
        to='Status',
        on_delete=models.PROTECT,
    )
    quality = models.ForeignKey(
        verbose_name=_('quality'),
        to='Quality',
        on_delete=models.PROTECT,
    )
    portals = models.ManyToManyField(
        to='Portal',
        verbose_name=_('portals'),
        through='PortalLink',
    )
    buyer = models.TextField(
        verbose_name=_('buyer'),
        blank=True,
    )
    price_min = models.DecimalField(
        verbose_name=_('price minimum'),
        blank=True, null=True,
        max_digits=8, decimal_places=2
    )
    price = models.DecimalField(
        verbose_name=_('price'),
        blank=True, null=True,
        max_digits=8, decimal_places=2
    )
    shipping = models.DecimalField(
        verbose_name=_('shipping costs'),
        blank=True, null=True,
        max_digits=4, decimal_places=2
    )
    categories = models.ManyToManyField(
        verbose_name=_('categories'),
        to='Category',
    )
    location = models.TextField(
        verbose_name=_('location'),
        blank=True,
    )
    notes = models.TextField(
        verbose_name=_('notes'),
        blank=True,
    )
    image_1 = models.URLField(
        verbose_name=_('image 1'),
        blank=True,
        max_length=1000,
    )
    image_2 = models.URLField(
        verbose_name=_('image 2'),
        blank=True,
        max_length=1000,
    )
    image_3 = models.URLField(
        verbose_name=_('image 3'),
        blank=True,
        max_length=1000,
    )
    image_4 = models.URLField(
        verbose_name=_('image 4'),
        blank=True,
        max_length=1000,
    )
    image_5 = models.URLField(
        verbose_name=_('image 5'),
        blank=True,
        max_length=1000,
    )

    def __str__(self):
        return self.name

    def thumbnail(self):
        url = self.link or self.image_1
        image = self.image_1
        return format_html('<a href="{}" target="_blank"><img src="{}" style="max-height: 6rem" /></a>', url, image)
