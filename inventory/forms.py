# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field, Submit
# from django.forms import ModelForm, CharField, Form
#
# from .models import Item
#
#
# class ItemFilterForm(Form):
#     name = CharField(required=False)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         # # Update the tags field to use the custom django-autocomplete's create field
#         # tags_queryset = self.fields.get('tags').queryset
#         # self.fields['tags'] = TagsCreateFormField(tags_queryset, required=False)
#         for key in self.fields:
#             self.fields[key].required = False
#
#         # for field in self.Meta.fields:
#         #     self.fields[field].required = False
#         #     self.fields[field].widget.attrs['required'] = 0
#
#         self.helper = FormHelper()
#         self.helper.form_method = 'GET'
#         self.helper.form_class = 'filter-form'
#         # self.helper.form_class = 'form-inline'
#         # self.helper.field_template = 'bootstrap3/layout/inline_field.html'
#
#         self.helper.layout = Layout(
#             Field('name'),
#             Field('categories'),
#         )
#         self.helper.add_input(Submit('filter', 'Filter'))
