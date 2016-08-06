from django.contrib import admin
from .models import Item, Portal, PortalLink, Status, Category

__author__ = 'eraldo'

admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Portal)
admin.site.register(PortalLink)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'name', 'status', 'price_min', 'price']
    list_filter = ['status', 'price', 'categories']
    readonly_fields = ['thumbnail']
    fields = (
        'thumbnail',
        'name', 'description',
        'status', 'buyer',
        # ('status', 'portals', 'buyer'),
        ('price', 'shipping', 'price_min'),
        'categories', 'location', 'notes',
        'link',
        'image_1', 'image_2', 'image_3', 'image_4', 'image_5',
    )


admin.site.register(Item, ItemAdmin)
