from django import forms
from mainapp import models

class loginform(forms.Form):
    username = forms.CharField(min_length=4,max_length=15)
    password = forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=16)

class signupform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, help_text="Password length must be between 8-16")
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.appuser
        fields = '__all__'
        widgets = {
        		'slug' : forms.HiddenInput(),
        }
        labels = {
            'tags' : 'Interest',
        }
        help_texts = {
            'username' : 'Username length must be 4-15.',
            'password' : 'Username length must be 8-16.',
        }

class askdoubt(forms.ModelForm):
    class Meta:
        model = models.doubts
        fields = '__all__'
        widgets = {
            'author' : forms.HiddenInput(),
        }