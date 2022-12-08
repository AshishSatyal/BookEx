from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter your email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your password'}))
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("MAKE SURE YOUR PASSWORD MATCHES!")