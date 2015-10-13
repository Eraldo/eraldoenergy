from django.contrib import admin
from .models import Instructor, Group


__author__ = 'eraldo'


admin.site.register(Group)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'gender', 'partner', 'group', 'country', 'has_url')

admin.site.register(Instructor, InstructorAdmin)
