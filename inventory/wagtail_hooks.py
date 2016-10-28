from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Item


@modeladmin_register
class InstitutionModelAdmin(ModelAdmin):
    model = Item
    menu_label = _('Inventory')
    menu_icon = 'list-ul'
    list_display = ('thumbnail', 'name', 'status', 'quality', 'price_min', 'price')
    search_fields = ('name', 'description')
    list_per_page = 40
