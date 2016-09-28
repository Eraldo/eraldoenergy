from django.db import ProgrammingError
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from .blocks import BASE_BLOCKS


class UniquePageMixin(object):
    """
    Mixin for Wagtail pages to make sure only one of this Page exists.
    """

    @classmethod
    def clean_parent_page_models(cls):
        # Only allow a single instance.
        try:
            if cls.objects and cls.objects.exists():
                return []
        except ProgrammingError:  # not migrated yet.
            pass
        return super().clean_parent_page_models()


class ContentPage(Page):
    template = 'cms/page.html'

    content = StreamField(
        BASE_BLOCKS,
        blank=True
    )

    class Meta:
        verbose_name = _('Content')

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]
