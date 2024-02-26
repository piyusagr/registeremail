from django.shortcuts import render
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def register_user(request):
    if request.method=='POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            subject = 'Welcome to My Site'
            message = 'Thank you for registering!'
            from_email = settings.EMAIL_HOST_USER 
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)

   
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
