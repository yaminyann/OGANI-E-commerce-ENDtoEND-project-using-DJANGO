from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, 
    PasswordResetForm, PasswordChangeForm
    )
from . models import Customar,Newsletter,Contact
from django.utils.translation import gettext, gettext_lazy as _



# Signup form
class SignUp(UserCreationForm):
    email = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={'class':'form-control'})
        )
    password1 = forms.CharField(
        label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'})
        )
    password2 = forms.CharField(
        label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'})
        )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        label = {'email':'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'})
        }
        
# Login form
class Login(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})
        )
    password = forms.CharField(
        label=_('Password'),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-control'})
        )
    
    
# Password reset email send form
class Email_Submit_Form(PasswordResetForm):
    email = forms.EmailField(
        label=_('Enter your email'),
        max_length=50,
        widget=forms.EmailInput(
            attrs={'autocomplete':'email','class':'form-control'}
            )
        )
    
# Customar Registration Form
class Customar_Registration(forms.ModelForm):
    class Meta:
        model = Customar
        fields = ['name','division','district','zipcode','area','mobile','effective_delivery']
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder':'enter your name','class':'form-control'}
                ),
            'division': forms.Select(
                attrs={'class':'form-control'}
                ),
            'district': forms.Select(
                attrs={'class':'form-control'}
                ),
            'zipcode': forms.TextInput(
               attrs={'placeholder':'enter your Zip/post code','class':'form-control'}
            ),
            'area': forms.TextInput(
                 attrs={'placeholder':'enter your area','class':'form-control'}
            ),
            'mobile': forms.TextInput(
                attrs={'class':'form-control'}),
            'effective_delivery': forms.Select(
                attrs={'placeholder':'enter your area','class':'form-control'}),
            
        }
    
# password change form 
class passwordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(strip=False, widget=forms.PasswordInput(
            attrs={
                'auto complete':'current-password',
                'autofocus':True,
                'class':'form-control'
                }
        )
    )
    new_password = forms.CharField(strip=False, widget=forms.PasswordInput(
            attrs={
                'auto complete':'new password',
                'autofocus':True,
                'class':'form-control'
                }
        ),help_text=password_validation.password_validators_help_text_html
    )
    confirm_password = forms.CharField(strip=False, widget=forms.PasswordInput(
            attrs={
                'auto complete':'new password',
                'autofocus':True,
                'class':'form-control'
                }
        )
    )
    
# newsletter
class Newsletter_form(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your mail'})
        }

# Contact Form
class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']
        Widgets = {
           'name':forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter name'})),
           'email':forms.EmailInput(attrs={'placeholder':'Enter your mail'}),
           'message':forms.TextInput(attrs={'placeholder':'enter your comment'})
        }
        