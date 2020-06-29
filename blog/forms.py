from .models import Blog
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField



class BlogForm(forms.ModelForm):
    class Meta:
        model   =   Blog
        fields  =   ['content',]
'''
class BlogForm(forms.Form):
    title   =   forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Blog Heading',
        'class': 'form-control'
    }))
    content =   forms.CharField(
        widget=(
            MarkdownWidget(),
            SummernoteWidget()
            )
    content2 = MarkdownFormField()

'''