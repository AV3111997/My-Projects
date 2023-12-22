from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
from django.contrib import messages

# Create your views here.

def user_login(request):
    context = {}
    if request.method == 'GET':
        context['form'] = AuthenticationForm()
        return render(request, 'accounts/login.html', context)
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, 'You are now logged in.')
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('/')
    context['form'] = form
    return render(request, 'accounts/login.html', context)


def register(request):
    context = {}
    if request.method == 'GET':
        context['form'] = UserRegistrationForm()
        return render(request, 'accounts/register.html', context)
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        user = form.save(commit = False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request, 'Registration Successfull')
        return redirect('login')
    context['form'] = form
    return render(request, 'accounts/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('/')