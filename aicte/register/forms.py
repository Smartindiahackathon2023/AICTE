from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Developer,Institute


      

class CreateEducatorForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    institute = forms.ModelChoiceField(queryset=Institute.objects.all())
        

        
