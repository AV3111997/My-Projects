from django.urls import path
from .views import *

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/update/<int:id>/', category_update, name='category_update'),
    path('category/delete/<int:id>/', category_delete, name='category_delete'),

    path('product/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/update/<int:id>/', product_update, name='product_update'),
    path('product/delete/<int:id>/', product_delete, name='product_delete'),

    path('developer/', dev_list, name='dev_list'),
    path('developer/create/', dev_create, name='dev_create'),
    path('developer/update/<int:id>/', dev_update, name='dev_update'),
    path('developer/delete/<int:id>/', dev_delete, name='dev_delete'),
    
    path('publisher/', publisher_list, name='publisher_list'),
    path('publisher/create/', publisher_create, name='publisher_create'),
    path('publisher/update/<int:id>/', publisher_update, name='publisher_update'),
    path('publisher/delete/<int:id>/', publisher_delete, name='publisher_delete'),

    path('news/', admin_news_list, name='admin_news_list'),
    path('news/create/', create_news, name='news_create'),
    path('news/update/<int:id>/', news_update, name='news_update'),
    path('news/delete/<int:id>', news_delete, name='news_delete'),
    path('contact/', admin_contact, name='admin_contact'),

    path('users/', users_list, name='users_list'),
    path('users/delete/<int:id>/', user_delete, name='user_delete'),
]