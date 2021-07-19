from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, Post

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['profile_pic']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'content', 'image'
        ]