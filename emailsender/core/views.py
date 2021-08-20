from emailsender.core.models import Message
from django.http.response import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from emailsender.core.forms import MessageForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    context = {'message': MessageForm()}
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if not form.is_valid():
            return render(request, 'index.html', {'message': form})

        # Check if a sender was declared
        body = sanitize(form)
        html_body = sanitize_html(form)

        # Send email and insert the data into the model
        mail.send_mail(
            'Você recebeu uma carta!',  # subject
            body,  # message
            settings.DEFAULT_FROM_EMAIL,  # from email
            [settings.DEFAULT_FROM_EMAIL, form.cleaned_data['email']],  # recipient list
            html_message=html_body
        )

        Message.objects.create(**form.cleaned_data)

        # Success feedback to user
        messages.success(request, 'Sua carta foi enviada!')

        return HttpResponseRedirect('')


def sanitize(form):
    if form.cleaned_data['sender']:
        body = render_to_string('message_email.txt', form.cleaned_data)
    else:
        body = render_to_string('message_email_nofrom.txt', form.cleaned_data)
    return body


def sanitize_html(form):
    if form.cleaned_data['sender']:
        html_body = render_to_string('message_email.html', form.cleaned_data)
    else:
        html_body = render_to_string(
            'message_email_nofrom.html', form.cleaned_data)
    return html_body
