from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
#from blog.models import Series


class RegisterForm(UserCreationForm):
    class Meta:
        model   =   User
        fields  =   ['username','email']


class ProfileUpdate(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'rows':'6',
        'class': 'form-control',
        'placeholder':'Write a Short Bio'
    }))
    class Meta:
        model   =   User
        fields  =   ['bio']

class BioUpdate(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'rows':'6',
        'class': 'form-control',
        'placeholder':'Write a Short Bio'
    }))
    class Meta:
        model   =   User
        fields  =   ['bio',]


########## SERIES RELATED
# class SeriesForm(forms.ModelForm):
#     class Meta:
#         model  =  Series
#         fields  =   ['title',]