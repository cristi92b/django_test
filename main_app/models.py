from django.db import models
#Import ModelForm
from django import forms
from django.forms import ModelForm
#Import UserCreationForm and User model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Import i18n dependencies
from django.utils.translation import gettext
#Import Romania local fields
from localflavor.ro.forms import ROCountySelect, ROCountyField, ROPostalCodeField, ROCIFField
#Import EmailValidator
from django.core.validators import EmailValidator, RegexValidator, MinLengthValidator

# Create your models here.
class MainPage(models.Model):
    name = models.TextField()
    display_name = models.TextField()

class RegistrationModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    birthdate = models.DateField()
    country = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class RegistrationForm(ModelForm):
    class Meta:
        model = RegistrationModel
        fields = ["first_name", "last_name", "email", "password", "phone", "birthdate", "country", "post_code", "address"]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = forms.EmailField(validators=[EmailValidator(message="Enter a valid email address.")])
    phone = forms.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^(\+4)?\d{10}$', message="Phone number must be entered in the format: '+40723456789' or '0723456789'.")
    ], required=False)  # Optional field
    message = forms.CharField(widget=forms.Textarea, validators=[MinLengthValidator(2)])
