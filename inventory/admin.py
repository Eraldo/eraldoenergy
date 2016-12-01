from django.contrib import admin
from django.utils.html import format_html
from django.contrib.sites.models import Site

from .models import Item, Portal, PortalLink, Status, Quality, Category

__author__ = 'eraldo'

admin.site.register(Status)
admin.site.register(Quality)
admin.site.register(Category)
admin.site.register(Portal)
admin.site.register(PortalLink)


class PortalLinkInline(admin.TabularInline):
    model = PortalLink


class ItemAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'name', 'status', 'quality', 'price_min', 'price', 'price_original']
    list_display_links = ['name']
    list_filter = ['status', 'quality', 'categories']
    list_editable = ['status', 'quality', 'price', 'price_original']
    search_fields = ['name', 'description']
    readonly_fields = ['thumbnail', 'frontend']
    list_per_page = 40
    fields = (
        'thumbnail',
        'name', 'description',
        'status', 'quality', 'buyer',
        # ('status', 'portals', 'buyer'),
        ('price', 'shipping', 'price_min', 'price_original'),
        'categories', 'location', 'notes',
        'link',
        'image_1', 'image_2', 'image_3', 'image_4', 'image_5',
        'frontend',
    )
    inlines = [PortalLinkInline]

    def frontend(self, obj):
        url = ''
        if obj.url:
            domain = Site.objects.get_current().domain
            link = 'www.{0}{1}'.format(domain, obj.url)
            url = format_html('<a href="{0}" target="_blank">{0}</a>', link)
        return url


    def get_readonly_fields(self, request, obj=None):
        user = request.user
        if user.is_superuser:
            return self.readonly_fields
        else:
            return self.readonly_fields + ['price_min']

    # def get_changelist_formset(self, request, **kwargs):
    #     user = request.user
    #     if user.is_superuser:
    #         self.list_editable += ['price_min']
    #     return super().get_changelist_formset(request, **kwargs)


admin.site.register(Item, ItemAdmin)
