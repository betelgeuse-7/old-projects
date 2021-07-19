from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm, PostForm
from .models import Post
from django import forms

from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import time

def index(request):
    return render(request, 'base.html')



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit = False)
            user.set_password(user.password)  #set_password to set a 'raw' password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            return redirect('/registration')
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('usermodel:successful_login_page'))
            else: 
                return HttpResponse('The account is not active')
        else: 
            return HttpResponse('Invalid user information.')

    else:
        return render(request, 'login.html')

@login_required #Only logged-in users can sign out 
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('usermodel:index_page'))

@login_required
def logged_in(request):
    return render(request, 'success.html')

@login_required
def send_a_post(request):
    if request.method == 'POST':
        form = PostForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            form.save()
        else:
            return redirect('/')

    return render(request, 'post.html', {'posts': Post.objects.all(), 'form': PostForm()})

@login_required
def delete_a_post(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.user == post.author:
        post.delete()
        return redirect('/posts')
    else:
        raise forms.ValidationError('You are not the author of the post')