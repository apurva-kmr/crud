from django import forms
from django.contrib.auth.models import User
from orderapp.models import Coustumer

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class CoustumerForm(forms.ModelForm):
    class Meta:
        model=Coustumer
        fields='__all__'

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
