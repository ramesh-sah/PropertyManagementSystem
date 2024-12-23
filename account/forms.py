from django import forms
from .models import User


class UserRegisterForm(forms.Modelform):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

