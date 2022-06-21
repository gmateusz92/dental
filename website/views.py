from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(request):
    trans = translate(language='nl')
    return render(request, 'home.html', {trans:'trans'})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('We Believe Everyone Should Have Easy Access To Great Dental Care')
    finally:
        activate(cur_language)
    return text

def contact(request):
    if request.method == "POST":
        #do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send email
        send_mail(
            message_name, #subject
            message_email, # message
            message, # from email
            ['gmateusz92@gmail.com'], # to email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_name':message_name})
    else:
        # return the page
        return render(request, 'contact.html', {})