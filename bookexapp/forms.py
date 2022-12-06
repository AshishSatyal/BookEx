from django import forms
from django.contrib.auth.models import User
from bookexapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter your email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your password'}))
    
    class Meta():
        model = User
        # adding fields other then the default ones
        fields = ('username', 'email', 'password')
    # if password != confirm_password:
    #     raise forms.ValidationError("MAKE SURE YOUR PASSWORD MATCHES!")