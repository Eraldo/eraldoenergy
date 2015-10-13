from django.contrib import messages
from django.views.generic import FormView, TemplateView
from .forms import ContactForm

__author__ = "Eraldo Helal"


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = '.'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        messages.success(self.request, 'Your message has been sent.')
        return super(ContactView, self).form_valid(form)


class T42View(TemplateView):
    template_name = "contact/T42.html"
