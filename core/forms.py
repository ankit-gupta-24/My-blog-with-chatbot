from django.forms import ModelForm
from django import forms
from .models import ContactMessages



class ContactForm(ModelForm):
    class Meta:
        model = ContactMessages
        fields = ['name','mobile_number','email','message']
        widgets = {
            
            'name': forms.TextInput(
                attrs={
                    'class':"form-control ",
                    'placeholder': 'Enter your name',
                }
            ),

            'mobile_number': forms.NumberInput(
                attrs={
                    'class':"form-control ",
                    'placeholder': 'Enter your Mobile Number',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class':"form-control ",
                    'placeholder': 'Enter your Email ID',
                }
            ),

            'message':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Have any message ...',
                }
            )
        }
