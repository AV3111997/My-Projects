from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news_list'),
    path('news/<id>/', news_read, name='view'),
    path('contact/', contact, name='user_contact'),
    path('result/', search, name='search'),
    path('cart/', cart_home, name='cart_list'),
    path('cart/add/<int:id>', cart_add, name='cart_add'),
    path('cart/remove/<int:id>', cart_remove, name='cart_remove'),
    path('cart/delete/<int:id>', cart_delete, name='cart_delete'),
    path('wishlist/', wishlist_index, name='wishlist_main'),
    path('wishlist/add/<int:id>', wishlist_add, name='wishlist_add'),
    path('wishlist/remove/<int:id>', wishlist_remove, name='wishlist_remove'),
    path('wishlist/delete/<int:id>', wishlist_delete, name='wishlist_delete'),
    path('games/', library_home, name='library_list'),
    path('games/add/<int:id>', library_add, name='library_add'),
    path('games/delete/<int:id>', library_delete, name='library_delete'),
    path('category/<id>/', category_selection, name='category_selection'),
]