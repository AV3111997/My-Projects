from django.shortcuts import render
from . models import TravelPackage

# Create your views here.

def index(request):
    context = {}
    packages = TravelPackage.objects.all()
    context['packages'] = packages
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def services(request):
    context = {}
    return render(request, 'services.html', context)

def packages(request):
    context = {}
    packages = TravelPackage.objects.all()
    context['packages'] = packages
    return render(request, 'packages.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def booking(request):
    context = {}
    return render(request, 'booking.html', context)

def destination(request):
    context = {}
    return render(request, 'destination.html', context)

def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)

def guides(request):
    context = {}
    return render(request, 'guides.html', context)

def testimonials(request):
    context = {}
    return render(request, 'testimonials.html', context)

def tour(request):
    context = {}
    return render(request, 'tour.html', context)

