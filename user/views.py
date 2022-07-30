from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

import user
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} Account has been created")
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form 
    }
    return render(request, 'user/register.html', context)

def profile(request):
   
    return render(request, 'user/profile.html', {})


def profile_update(requests):
    if requests.method == 'POST':
        user_form = UserUpdateForm(requests.POST, instance=requests.user)
        profile_form = ProfileUpdateForm(requests.POST, requests.FILES, instance=requests.user.profile)

        if user_form.is_valid() & profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')


    else:
        user_form = UserUpdateForm(instance=requests.user)
        profile_form = ProfileUpdateForm(instance=requests.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form

    }

    return render(requests, 'user/profile_update.html', context)