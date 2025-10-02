from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import MainPage
from .models import RegistrationForm
from .models import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



# @api_view(['GET'])
# def homePage(request):
#     pages = MainPage.objects.all()
#     return render(request,"base.html", context = {'pages': pages})

def login_user(request):
    if request.method == "POST":
        print(request)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_app:home')
        else:
            #messages.success(request,"Login error!")
            return redirect('main_app:contact')
    else:
        return render(request,'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('main_app:home')

def register_user(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, "register.html", context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Send an email
            send_mail(
                f'[Django] Mesaj de la: {name}',
                f'De la: {name}\nMesaj: {message}\nTelefon: {phone}\nEmail: {email}',
                settings.EMAIL_HOST_USER,  # From email
                [settings.ADMIN_EMAIL],  # To email
                fail_silently=False,
            )

            return redirect('main_app:contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
  return HttpResponse('Success!')

#class RegisterPageView(TemplateView):
#    template_name = "register.html"

class MainPageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        pages = MainPage.objects.all()
        context = {'pages': pages}
        return context

class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        pages = MainPage.objects.all()
        context = {'pages': pages}
        return context

class AboutPageView(TemplateView):
    template_name = "base.html"

class ContactPageView(TemplateView):
    template_name = "base.html"

class ServicesPageView(TemplateView):
    template_name = "base.html"
