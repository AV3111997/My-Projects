from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_list, name='cart_list'),
    path('cart/add/<int:id>', views.cart_add, name='cart_add'),
    path('cart/remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('cart/delete/<int:id>', views.cart_delete, name='cart_delete'),
    path('cart/update/<int:id>', views.cart_item_update, name='cart_item_update'),
    path('cart/buy/<int:id>', views.buy_cart_item, name='buy_cart_item'),
]