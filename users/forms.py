from django import forms
from . models import Account
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'mobile_number', 'email', 'password1', 'password2', 'address']


# class ProfileUpdateForm(forms.ModelForm):

#     class Meta:
#         model = Account
#         fields = ['email', 'address', 'mobile_number', 'image']
