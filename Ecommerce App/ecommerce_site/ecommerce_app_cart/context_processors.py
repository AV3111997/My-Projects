from .models import Cart
from django.db.models import Sum, IntegerField
from django.db.models import F, ExpressionWrapper, FloatField

def cart_item_counters(request):
    cart_items_count = 0
    if request.user.is_authenticated:
        cart_items_count = Cart.objects.filter(user=request.user).aggregate(total_items=Sum('quantity'))['total_items'] or 0

    return {'cart_items_count': cart_items_count}

def cart_checkout(request):
    totalamount = 0
    if request.user.is_authenticated:
        totalamount = Cart.objects.filter(user=request.user).aggregate(total_amount=Sum('totalcost'))['total_amount'] or 0

    return {'totalamount': totalamount}
        

