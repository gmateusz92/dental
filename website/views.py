from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        #do styff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        return render(request, 'contact.html', {'message_name':message_name})
    else:
        # return the page
        return render(request, 'contact.html', {})