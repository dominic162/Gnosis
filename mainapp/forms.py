from django import forms
from mainapp import models

class loginform(forms.Form):
    username=forms.CharField(min_length=4,max_length=15)
    password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=16)

class signupform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=models.appuser
        fields='__all__'
        widgets = {
        		'slug': forms.HiddenInput(),
        }