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
    list_display_links = ['name']
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
