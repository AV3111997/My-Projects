from django import http
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . models import Cart
from ecommerce_app.models import Product

# Create your views here.

@login_required(login_url='/accounts/login/')
def cart_list(request):
    context = {
        'cart_list': Cart.objects.filter(user=request.user).select_related('product'),
    }
    return render(request, 'cart/list.html', context)

@login_required(login_url='/accounts/user_authentication')
def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart.objects.filter(user=request.user, product=product).first()

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        totalcost = float(request.POST.get('totalcost'))

        if not cart:
            cart = Cart.objects.create(user=request.user, product=product, quantity=quantity, totalcost=totalcost)
        else:
            if cart.quantity + quantity <= product.stock:
                cart.quantity += quantity
                cart.save()
        return redirect('cart_list')

    return render(request, 'cart/cart_add.html', {'product': product, 'cart': cart})
    

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
def buy_cart_item(request, id):
    item = get_object_or_404(Cart, id=id, user=request.user)
    return redirect('cart_list')

@login_required(login_url='/accounts/login/')
def cart_item_update(request, id):
    user = request.user  # Get the current user
    cart_item = get_object_or_404(Cart, id=id, user=user)  # Fetch the specific cart item for the current user

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        # No need for totalcost if it's calculated based on quantity * product price in the model itself

        if cart_item:
            if cart_item.quantity <= cart_item.product.stock:
                cart_item.quantity = quantity
                cart_item.totalcost = quantity * cart_item.product.price
                cart_item.save()
        
        return redirect('cart_list')  

    return render(request, 'cart/cart_update.html', {'cart_item': cart_item})
