from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs =
        {
            'class' : 'form-control',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs =
        {
            'class' : 'form-control'
        }
    ))


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs =
        {
        'class' : 'form-control',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs =
        {
        'class' : 'form-control',
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs =
        {
            'class' : 'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs =
        {
        'class' : 'form-control',
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs =
        {
        'class' : 'form-control'
        }
    ))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(
        attrs =
        {
        'class' : 'form-control'
        }
    ))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs =
        {
        'class' : 'form-control',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs =
        {
        'class' : 'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs =
        {
        'class' : 'form-control col-lg-6',
        }
    ))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.ClearableFileInput(
        attrs =
        {
        'class' : 'form-control',
        }
    ))
    class Meta:
        model = Profile
        fields = ('photo',)
