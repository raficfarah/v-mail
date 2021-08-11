from django.http.response import HttpResponse, HttpResponseRedirect
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from emailsender.core.forms import MessageForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():

            body = render_to_string('message_email.txt', form.cleaned_data)

            mail.send_mail('Você recebeu uma carta!',
                        body,
                        'elegante.correios.01@gmail.com',
                        ['raficfarah07@gmail.com', form.cleaned_data['email']])

            messages.success(request, 'Sua carta foi enviada!')

            return HttpResponseRedirect('')
        else:
            return render(request, 'index.html', {'message': form})

    else:
        context = {'message': MessageForm()}
        return render(request, 'index.html', context)
