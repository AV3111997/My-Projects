from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
# Create your views here.

def register(request):
    context={}
    if request.method == 'GET':
        context['form'] = UserRegistrationForm()
        return render(request, 'register.html', context)
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        user = form.save(commit = False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    context['form'] = form
    return render(request, 'register.html', context)


# def login_view(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = UserLoginForm()
#         return render(request, 'login.html', context)
#     form = UserLoginForm(data=request.POST)
#     if form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         return redirect('/')
#     else:
#         messages.error(request, 'Invalid user credentials. Please try again.')
#         context['form'] = form
#         return render(request, 'login.html', context)  
    
def login_view(request):
    context = {}
    if request.method == 'GET':
        context['form'] = UserLoginForm()
        return render(request, 'login.html', context)
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        username = form.data['username']
        password = form.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'INVALID USER!')
            return redirect('login')   
    context['form'] = form
    return render(request, 'login.html', context)  

def user_logout(request):
    logout(request)
    return redirect('/')

def user_authentication(request):
    return render(request, 'user_authentication.html')






9

    
