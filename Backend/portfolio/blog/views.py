from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for contacting us!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list="ajaysinghdodiya29@gmail.com",  # Replace with your email
                fail_silently=False,
            )

            # Redirect to a success page
            return redirect('contact_success')  # Define this route in urls.py
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
