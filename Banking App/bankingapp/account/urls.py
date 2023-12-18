from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),  
    path('logout/',views.logout, name='logout'),
    path('account_apply/', views.account_apply, name='account_apply'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('success_page/', views.success_page, name='success_page'),
]