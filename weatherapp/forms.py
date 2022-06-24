from django.forms import ModelForm, TextInput
from .models import City
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CityForm(ModelForm):
    class Meta:
        model=City
        fields={'name'}
        widgets = {
            'name': TextInput(attrs={'placeholder': 'City Name','class':'form-control'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]