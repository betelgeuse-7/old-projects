from django import forms
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'text'
        ]


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username'
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'
        ]
