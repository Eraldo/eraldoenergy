from autoslug import AutoSlugField
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from cms.blocks import BASE_BLOCKS
from cms.models import UniquePageMixin


@register_snippet
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


@register_snippet
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


@register_snippet
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
        return str(self.portal)


def image_path(instance, filename):
    pass


class Item(models.Model):
    name = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        unique=True,
    )
    slug = AutoSlugField(
        populate_from='name',
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
    price_original = models.DecimalField(
        verbose_name=_('original price'),
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

    @property
    def images(self):
        images = []
        for attribute in ['image_1', 'image_2', 'image_3', 'image_4', 'image_5']:
            image = getattr(self, attribute)
            if image:
                images.append(image)
        return images

    def __str__(self):
        return self.name

    @property
    def url(self):
        if not self.slug:
            self.save()
        return reverse('inventory:detail', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return self.url

    def thumbnail(self):
        url = self.link or self.image_1
        image = self.image_1
        return format_html('<a href="{}" target="_blank"><img src="{}" style="max-height: 6rem" /></a>', url, image)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('link'),
        FieldPanel('status'),
        FieldPanel('quality'),
        # FieldPanel('portals'),
        # InlinePanel('portals'),
        FieldPanel('buyer'),
        FieldPanel('price_min'),
        FieldPanel('price_original'),
        FieldPanel('price'),
        FieldPanel('shipping'),
        FieldPanel('categories'),
        FieldPanel('location'),
        FieldPanel('notes'),
        MultiFieldPanel(
            [
                FieldPanel('image_1'),
                FieldPanel('image_2'),
                FieldPanel('image_3'),
                FieldPanel('image_4'),
                FieldPanel('image_5'),
            ],
            heading="Images",
            classname="collapsible"
        ),
    ]


class InventoryPage(UniquePageMixin, Page):
    template = 'inventory/index.html'

    content = StreamField(
        BASE_BLOCKS,
        blank=True
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        items = Item.objects.exclude(status__name__in=['sold', 'shipped', 'done'])
        paginator = Paginator(items, 20)  # Show 20 contacts per page

        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            items = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            items = paginator.page(paginator.num_pages)
        context['items'] = items

        return context

    class Meta:
        verbose_name = _('Inventory')

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]
