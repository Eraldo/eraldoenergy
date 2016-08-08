from django.contrib import admin
from .models import Item, Portal, PortalLink, Status, Quality, Category

__author__ = 'eraldo'

admin.site.register(Status)
admin.site.register(Quality)
admin.site.register(Category)
admin.site.register(Portal)
admin.site.register(PortalLink)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'name', 'status', 'quality', 'price_min', 'price']
    list_filter = ['status', 'quality', 'categories']
    list_editable = ['status', 'quality', 'price']
    readonly_fields = ['thumbnail']
    list_per_page = 40
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
