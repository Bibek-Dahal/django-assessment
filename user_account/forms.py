from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
import re
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    
    # username = forms.CharField(min_length=3,widget=forms.TextInput(attrs={"placeholder":"enter your name"}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        max_length=25,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','placeholder':'enter password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )  
    password2 = forms.CharField(
            label=_("Password confirmation"),
            widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','placeholder':'re-enter password'}),
            max_length=25,
            strip=False,
            help_text=_("Enter the same password as before, for verification."),
    )   
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone_number')
    
        widgets ={
            
            'email':forms.EmailInput(attrs={"placeholder":"enter your email","minlength":11}),
        }
       

    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','phone_number')

    