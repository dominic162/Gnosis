from django import forms
from mainapp import models

class login_form(forms.Form):
    username = forms.CharField(min_length=4,max_length=15)
    password = forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=16)

class signup_form(forms.ModelForm):
    password         = forms.CharField(widget=forms.PasswordInput, help_text="Password length must be between 8-16")
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model      = models.appuser
        fields     = '__all__'
        widgets    = {
        		'slug' : forms.HiddenInput(),
        }
        labels     = {
            'tags' : 'Interest',
        }
        help_texts = {
            'username' : 'Username length must be 4-15.',
            'password' : 'Username length must be 8-16.',
        }

class ask_doubt(forms.ModelForm):
    class Meta:
        model   = models.doubts
        fields  = '__all__'
        widgets = {
            'author' : forms.HiddenInput(),
        }

class new_book( forms.ModelForm ):
    class Meta:
        model   = models.book
        fields  = '__all__'
        widgets = {
            'uploaded_by' : forms.HiddenInput(),
        } 

class contact_form( forms.ModelForm ):
    class Meta:
        model  = models.contact
        fields = '__all__'

class links_info( forms.ModelForm ):
    class Meta:
        model  = models.extra_info
        fields = '__all__'
