from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactModel


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'product.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            con = ContactModel(name=name, email=email, message=message)
            con.save()
            return redirect('home')  # Redirect to the main page
        else:
            messages.error(request, 'Please provide all the required information.')
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')