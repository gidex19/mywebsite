from django.shortcuts import render
from .forms import ContactForm
from .models import Customer
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def services(request):
    return render(request, 'portfolio/services.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            details = form.cleaned_data.get('details')
            software_type = form.cleaned_data.get('software_type')
            category = form.cleaned_data.get('category')

            Customer.objects.create(full_name=full_name, email=email, phone_number=phone_number, details=details, software_type=software_type,
                                    category=category)
            messages.success(request, 'Your message has been sent successfully. We will get back to You')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

