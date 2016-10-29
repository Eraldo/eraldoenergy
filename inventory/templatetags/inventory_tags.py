from classytags.helpers import InclusionTag
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.tag
class Item(InclusionTag):
    name = 'item'
    template = 'inventory/item.html'

    def get_context(self, context, **kwargs):
        item = context.get('item')
        if item:
            return {
                'name': item,
                'image': item.image_1,
                'price': item.price,
                'original_price': item.price * 2 if item.price else '',
                'id': item.pk,
            }
        else:
            return {}
