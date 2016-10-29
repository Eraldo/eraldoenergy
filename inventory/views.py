from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Item


class ItemListView(ListView):
    template_name = "inventory/list.html"
    model = Item
    context_object_name = 'items'
    paginate_by = 20


class ItemDetailView(DetailView):
    template_name = "inventory/item.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        if item:
            context['title'] = item.name
        return context
