#!/usr/bin/env python
"""
This module contains the web pages based views.
"""
from django.contrib import messages
from django.views.generic import TemplateView

__author__ = "Eraldo Helal"


class HomeView(TemplateView):
    template_name = "pages/home.html"


# topics


class PersonalDevelopmentView(TemplateView):
    template_name = "pages/personal-development.html"


class WebDesignView(TemplateView):
    template_name = "pages/web-design.html"


class TechnologyView(TemplateView):
    template_name = "pages/technology.html"


# misc


class ChatView(TemplateView):
    template_name = "pages/chat.html"


class TestView(TemplateView):
    template_name = "pages/test.html"

    def get(self, request, *args, **kwargs):
        messages.info(request, 'Welcome to the Legend of..')
        messages.success(request, 'AWESOME')
        messages.debug(request, 'debugging')
        messages.warning(request, 'Take care..')
        messages.error(request, 'This will change your life!')
        return super(TestView, self).get(request, *args, **kwargs)

