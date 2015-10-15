from django.contrib import admin
from .models import Event

__author__ = 'eraldo'


class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end', 'type', 'country', 'city', 'has_url')
    list_filter = ['type', 'country']

admin.site.register(Event, EventsAdmin)
