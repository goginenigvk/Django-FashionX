from django import forms
from .models import Contact


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

class PersonForm(forms.Form):
    name=forms.CharField(max_length=50,label='Enter your name ',initial="John", label_suffix=' :::::::::::')
    age=forms.IntegerField(label='Enter your age',required=False)
    gender=forms.CharField(widget=forms.RadioSelect)
    email=forms.EmailField(label='Enter your email',help_text='type email with .com')
    password=forms.CharField(label='Enter your password',widget=forms.PasswordInput)
    aboutu=forms.CharField(widget=forms.Textarea)
    birth = forms.DateField(widget=forms.SelectDateWidget)


class ContactForm(forms.ModelForm):
  
    class Meta: 
        model=Contact
        fields='__all__'


