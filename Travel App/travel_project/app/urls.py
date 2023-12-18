from django.urls import path
from . import views
# app_name = 'app'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('packages', views.packages, name='packages'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('booking', views.booking, name='booking'),
    path('destination', views.destination, name='destination'),
    path('gallery', views.gallery, name='gallery'),
    path('guides', views.guides, name='guides'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('tour', views.tour, name='tour'),
]