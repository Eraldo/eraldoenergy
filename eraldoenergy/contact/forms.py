from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Fieldset
from django import forms
from django.core.mail import send_mail

__author__ = 'Eraldo Helal'


class EmailField(Field):
    def render(self, *args, **kwargs):
        html = super(EmailField, self).render(*args, **kwargs)
        return html.replace('type="text"', 'type="email"', 1)


class ContactForm(forms.Form):
    email = forms.EmailField(label="email")
    message = forms.CharField(label="message", widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary

        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]

        # debug
        # print("should send email now to {} with message {}".format(email, message))

        # production
        subject = "[eraldo.org] message from '{}'".format(email)
        send_mail(subject, message, email, ['eraldo@eraldo.org'])

    helper = FormHelper()
    helper.html5_required = True
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Fieldset(
            'contact form',
            EmailField('email', css_class='form-control', placeholder="your email"),
            Field('message', rows="4", css_class='form-control', placeholder="your message", style="resize: vertical;"),
        ),
        HTML("""
        <br>
        <button type="submit" class="btn btn-lg btn-primary"><span class="glyphicon glyphicon-send"></span> send
            message
        </button>
         """),
    )
