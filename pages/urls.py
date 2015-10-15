#!/usr/bin/env python
"""
Contains the web pages related url mappings.
"""

__author__ = "Eraldo Helal"

from django.conf.urls import patterns, url
from django.shortcuts import redirect

from .views import HomeView, TestView, ChatView, PersonalDevelopmentView, WebDesignView, TechnologyView

urlpatterns = patterns('',
    # ex: ../
    url(r'^$',
        lambda x: redirect('home/'),
        name='redirect'),
    # ex: ../home/
    url(r'^home/$',
        HomeView.as_view(),
        name='home'),

    # TOPICS
    # ex: ../personal-development/
    url(r'^personal-development/$',
        PersonalDevelopmentView.as_view(),
        name='personal-development'),
    # ex: ../web-design/
    url(r'^web-design/$',
        WebDesignView.as_view(),
        name='web-design'),
    # ex: ../technology/
    url(r'^technology/$',
        TechnologyView.as_view(),
        name='technology'),

    # ex: ../chat/
    url(r'^chat/$',
        ChatView.as_view(),
        name='chat'),
    # ex: ../test/
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
)
