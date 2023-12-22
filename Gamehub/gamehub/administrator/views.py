from this import d
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseNotFound, HttpResponse
from .forms import *
from .models import *
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.

#CONTACT
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_contact(request):
    context = {
        'object_list': ContactUs.objects.all()
    }
    return render(request, 'administrator/contact/list.html', context)


#CATEGORY
@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_list(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'administrator/category/list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    context = {}
    if request.method == 'GET':
        context['form'] = CategoryForm()
        return render(request, 'administrator/category/create.html', context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            context['form'] = form
            return render(request, 'administrator/category/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_update(request, id):
    context = {}
    category = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        context['form'] = CategoryForm(instance=category)
        return render(request, 'administrator/category/create.html', context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            context['form'] = form
            return render(request, 'administrator/category/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')


#PRODUCT
@login_required
@user_passes_test(lambda u: u.is_superuser)
def product_list(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'administrator/product/list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    context = {}
    if request.method == 'GET':
        context['form'] = ProductForm()
        return render(request, 'administrator/product/create.html', context)
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context['form'] = form
            return render(request, 'administrator/product/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def product_update(request, id):
    context = {}
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        context['form'] = ProductForm(instance=product)
        return render(request, 'administrator/product/create.html', context)
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context['form'] = form
            return render(request, 'administrator/product/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.status = 'Inactive'
    product.save()
    return redirect('product_list')


#DEVELOPER
@login_required
@user_passes_test(lambda u: u.is_superuser)
def dev_list(request):
    context = {
        'object_list': Developer.objects.all()
    }
    return render(request, 'administrator/developer/list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def dev_create(request):
    context = {}
    if request.method == 'GET':
        context['form'] = DeveloperForm()
        return render(request, 'administrator/developer/create.html', context)
    elif request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dev_list')
        else:
            context['form'] = form
            return render(request, 'administrator/developer/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def dev_update(request, id):
    context = {}
    product = get_object_or_404(Developer, id=id)
    if request.method == 'GET':
        context['form'] = DeveloperForm(instance=product)
        return render(request, 'administrator/developer/create.html', context)
    elif request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dev_list')
        else:
            context['form'] = form
            return render(request, 'administrator/developer/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def dev_delete(request, id):
    product = get_object_or_404(Developer, id=id)
    product.status = 'Inactive'
    product.save()
    return redirect('dev_list')


#PUBLISHER
@login_required
@user_passes_test(lambda u: u.is_superuser)
def publisher_list(request):
    context = {
        'object_list': Publisher.objects.all()
    }
    return render(request, 'administrator/publisher/list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def publisher_create(request):
    context = {}
    if request.method == 'GET':
        context['form'] = PublisherForm()
        return render(request, 'administrator/publisher/create.html', context)
    elif request.method == 'POST':
        form = PublisherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
        else:
            context['form'] = form
            return render(request, 'administrator/publisher/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def publisher_update(request, id):
    context = {}
    product = get_object_or_404(Publisher, id=id)
    if request.method == 'GET':
        context['form'] = PublisherForm(instance=product)
        return render(request, 'administrator/publisher/create.html', context)
    elif request.method == 'POST':
        form = PublisherForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
        else:
            context['form'] = form
            return render(request, 'administrator/publisher/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def publisher_delete(request, id):
    product = get_object_or_404(Publisher, id=id)
    product.status = 'Inactive'
    product.save()
    return redirect('publisher_list')


#NEWS
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_news_list(request):
    context = {
        'object_list': News.objects.all(),
    }
    return render(request, 'administrator/news/list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_news(request):
    context = {}
    if request.method == 'GET':
        context['form'] = NewsForm()
        return render(request, 'administrator/news/create.html', context)
    elif request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'NEWS POSTED SUCCESSFULLY')
            return redirect('news_create')
        else:
            messages.success(request, 'NEWS POSTING FAILED')
            context['form'] = form
            return render(request,'administrator/news/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def news_delete(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return redirect('admin_news_list')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def news_update(request, id):
    context = {}
    news = get_object_or_404(News, id=id)
    if request.method == 'GET':
        context['form'] = NewsForm(instance=news)
        return render(request, 'administrator/news/create.html', context)
    elif request.method == 'POST':
        form = News(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            context['form'] = form
            return render(request, 'administrator/news/create.html', context)


#USER_MANAGER
@login_required
@user_passes_test(lambda u: u.is_superuser)
def users_list(request):
    context = {
        'object_list': User.objects.all(),
    }
    return render(request, 'administrator/users/list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users_list')




