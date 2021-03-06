# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from search.views import search

BACKEND_NAME = 'Eraldo Energy backend'
admin.site.site_header = BACKEND_NAME
admin.site.site_title = BACKEND_NAME

urlpatterns = [
    # Meta information
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^humans\.txt/$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
    # Django Admin, use {% url 'admin:index' %}
    url(r'^{}/'.format(settings.ADMIN_URL), include(admin.site.urls)),

    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    # url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # User management
    url(r'^users/', include('eraldoenergy.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^dance/', include('dance.urls', namespace='dance')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^items/', include('inventory.urls', namespace='inventory')),
    url(r'', include('pages.urls', namespace='pages')),

    # CMS wagtail
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search, name='search'),  # optional

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]
