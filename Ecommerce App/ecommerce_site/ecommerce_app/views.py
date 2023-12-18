from django.shortcuts import render, redirect, get_object_or_404
from . models import Category, Product, Outfit
from . forms import CategoryForm, ProductForm
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def index(request):
    products = Product.objects.filter(available=True)

    products_paginator = Paginator(products, 3)

    page_num = request.GET.get('page')

    page = products_paginator.get_page(page_num)

    context = {
        'count': products_paginator.count,
        'page':  page,
    }
    return render(request, 'index.html', context)

def product_page(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)

def products_by_category(request, category_slug=None):
    category_page = None
    products = None
    outfits = None
    if category_slug:
        category_page = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category_page,available=True)
        outfits = Outfit.objects.all()
        return render(request, 'category/category.html',{'category':category_page, 'products': products, 'outfits':outfits})


# def add_product(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = ProductForm()
#         return render(request, 'products/add_product.html', context)
#     form = ProductForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('product_page')
#     context['form'] = form
#     return render(request, 'products/add_product.html', context)
     
def category_page(request):
    context = {
        'category': Category.objects.all()
    }
    return render(request, 'category/category.html', context)

# def add_category(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = CategoryForm()
#         return render(request, 'category/add_category.html', context)
#     form = CategoryForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('category_page')
#     context['form'] = form
#     return render(request, 'category/add_category.html', context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__icontains=searched))
        context = { 
            'searched': searched,
            'searched_products': products,
        }
        return render(request,'search/result.html', context)
    else:
        return render('/')



