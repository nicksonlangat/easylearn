from .models import Blog
from django import forms


class BlogForm(forms.ModelForm):
    title   =   forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Blog Heading',
        'class': 'form-control'
    }))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':"Write your blog details here",
        'rows':'5'
    }))
    class Meta:
        model   =   Blog
        fields  =   ['title', 'content']