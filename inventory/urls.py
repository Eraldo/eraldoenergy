from django.conf.urls import url
from .views import ItemListView, ItemDetailView

__author__ = 'eraldo'

urlpatterns = [
    url(
        regex=r'^$',
        view=ItemListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=ItemDetailView.as_view(),
        name='detail'
    ),
]
