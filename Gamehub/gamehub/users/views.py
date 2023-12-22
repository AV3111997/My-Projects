from django import http
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from administrator.models import *
from administrator.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def index(request):
    products = Product.objects.all()

    products_paginator = Paginator(products, 8)

    page_num = request.GET.get('page')

    page = products_paginator.get_page(page_num)

    context = {
        'count': products_paginator.count,
        'page':  page,
        'object_list': Product.objects.all(),
        'news_object_list': News.objects.all()[:3],
        'category_object_list': Category.objects.all(),
    }
    return render(request, 'users/index.html', context)


def about(request):
    return render(request,'users/about.html')


def news(request):
    context = {
        'news_object_list': News.objects.all(),
    }
    return render(request,'users/news/list.html', context)


def news_read(request, id):
    context = {
        'object': News.objects.get(pk=id), 
    }
    return render(request,'users/news/view.html', context)

def category_selection(request, id):
    context = {
        'category_object': Category.objects.get(pk=id),
    }
    return render(request,'users/category/list.html', context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = Product.objects.filter(name__contains=searched)
        context = { 
            'searched': searched,
            'search_object_list': product,
        }
        return render(request,'users/search/result.html', context)
    else:
        return render('/')
        

@login_required(login_url='/accounts/login/')
def contact(request):
    context = {}
    if request.method == "GET":
        context['form'] = ContactForm()
        return render(request, "users/contact.html", context)
    elif request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('user_contact')
        else:
            context['form'] = form
            return render(request, "users/contact.html", context)


@login_required(login_url='/accounts/login/')
def wishlist_index(request):
    context = {
        'object_list': Wishlist.objects.filter(user=request.user).select_related('product'),
    }
    return render(request, 'users/wishlist/list.html', context)


@login_required(login_url='/accounts/login/')
def wishlist_add(request, id):
    product = get_object_or_404(Product, id=id)
    wish = Wishlist.objects.filter(user=request.user, product=product).first()
    if not wish:
        wish = Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, 'Item added to wishlist')
        return redirect('home')
    else:
        messages.error(request, 'Item already in wishlist')
        return redirect('home')

    
@login_required(login_url='/accounts/login/')
def wishlist_remove(request, id):
    wish = get_object_or_404(Wishlist, id=id, user=request.user)
    wish.delete()
    return redirect('wishlist_main')


@login_required(login_url='/accounts/login/')
def wishlist_delete(request, id):
    cart = get_object_or_404(Wishlist, id=id, user=request.user)
    cart.delete()
    return redirect('wishlist_main')


@login_required(login_url='/accounts/login/')
def cart_home(request):
    context = {
        'object_list': Cart.objects.filter(user=request.user).select_related('product'),
    }
    return render(request, 'users/cart/list.html', context)


@login_required(login_url='/accounts/login/')
def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart.objects.filter(user=request.user, product=product).first()
    if not cart:
        cart = Cart.objects.create(user=request.user, product=product, quantity=1)
        return redirect('cart_list')
    
    if cart.quantity < 5:
        cart.quantity += 1
        cart.save()
        return redirect('cart_list')


@login_required(login_url='/accounts/login/')
def cart_remove(request, id):
    cart = get_object_or_404(Cart, id=id, user=request.user)
    
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
        return redirect('cart_list')
    
    cart.delete()
    return redirect('cart_list')


@login_required(login_url='/accounts/login/')
def cart_delete(request, id):
    cart = get_object_or_404(Cart, id=id, user=request.user)
    cart.delete()
    return redirect('cart_list')


@login_required(login_url='/accounts/login/')
def library_home(request):
    context = {
        'object_list': Library.objects.filter(user=request.user).select_related('name'),
    }
    return render(request, 'users/library/list.html', context)


@login_required(login_url='/accounts/login/')
def library_add(request, id):
    product = get_object_or_404(Product, id=id)
    Library.objects.create(user=request.user, name=product)
    return redirect('cart_list')


@login_required(login_url='/accounts/login/')
def library_delete(request, id):
    game = get_object_or_404(Library, id=id, user=request.user)
    game.delete()
    return redirect('library_list')


