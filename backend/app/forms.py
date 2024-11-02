# your_app/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,  # Assuming a typical username length
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'username',
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'placeholder': 'Enter your password',
        })
    )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Enter your email',
        })
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password'
            }),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email addresses must be unique.")
        return email