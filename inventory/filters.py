from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django_filters import FilterSet

from .models import Item


class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = {
            'name': ['icontains'],
            'categories': ['exact'],
        }

    @property
    def form(self):
        form = super().form

        helper = FormHelper()
        helper.form_method = 'GET'

        helper.layout = Layout(
            Field('name__icontains'),
            Field('categories'),
        )
        helper.add_input(Submit('filter', 'Filter'))

        form.helper = helper
        return form
