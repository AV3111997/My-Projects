from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Account, District, Branch
from .forms import ApplicationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
                    username=username,
                    password=password
                )
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Incorrect username or password!")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if not username:
            messages.info(request,"Enter username.")
            return redirect('register')
        if not password:
            messages.info(request,"Enter a password!")
            return redirect('register')
        if not confirm_password:
            messages.info(request,"Enter confirm password!")
            return redirect('register')    
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken!")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                print("User created!")
            user.save()
        else:
            messages.info(request, "Password do not match!")
            return redirect('register')
        return redirect('login')
    return render(request,'register.html')


@login_required(login_url='/account/login/')
def account_apply(request):
    context = {}
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        materials_selected = request.POST.getlist('materials_provide')
        materials_concatenated = ', '.join(materials_selected)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.materials_provide = materials_concatenated
            instance.user = request.user 
            instance.save()
            return redirect('success_page')
        context['form'] = form
        return render(request, 'account_apply_form.html', context)
    context['form'] = ApplicationForm()
    return render(request, 'account_apply_form.html', context)
    
def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    branches_list = list(branches)
    return JsonResponse({'branches': branches_list})

def success_page(request):
    return render(request, 'success_page.html')