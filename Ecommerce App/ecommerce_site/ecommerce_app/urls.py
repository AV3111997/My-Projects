from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('products',views.product_page, name='product_page'),
    path('<slug:category_slug>',views.products_by_category, name='products_by_category'),
    # path('add_product',views.add_product, name='add_product'),
    path('category',views.category_page, name='category_page'),
    # path('add_category',views.add_category, name='add_category'),
    path('result/',views.search, name='search'),
]