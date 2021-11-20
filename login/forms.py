from django.contrib.auth.forms import UserCreationForm
from django import forms
from login.models import CustomUser


class signUpForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)

    class Meta:
        # username, password1, password2 are extended by User
        model = CustomUser
        fields = ('username', 'name', 'surname', 'email', 'password1', 'password2')