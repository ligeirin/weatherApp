from django.forms import ModelForm, ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class ConfigureForm(forms.Form):
    country = forms.CharField(label='Country', max_length=100)
    federation = forms.CharField(label='Federation', max_length=100)
    city = forms.CharField(label='City', max_length=100)

    def send(self):
        return { 'country': self.cleaned_data['country'], 'federation': self.cleaned_data['federation'], 'city': self.cleaned_data['city'] }