from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule, check_url, allow_without_attributes

__author__ = 'eraldo'


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'u': allow_without_attributes,
        'strike': allow_without_attributes,
        'a': attribute_rule({'href': check_url, 'target': True}),
    }
