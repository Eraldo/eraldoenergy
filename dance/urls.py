from django.conf.urls import url
from .views import DanceView

__author__ = 'eraldo'

urlpatterns = [
    # ex: ../dance/
    url(r'^$',
        DanceView.as_view(),
        name='home'),
]
