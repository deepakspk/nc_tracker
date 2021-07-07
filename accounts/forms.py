from .models import Admin
from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class AdminForm(ModelForm):
    class Meta:
        model= Admin
        exclude = ('status','user',)

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=254)