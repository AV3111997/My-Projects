from .models import Category, Outfit

def category_dropdown(request):
    categories = Category.objects.all() 
    return {'categories': categories}

def outfit_type(requets):
    outfits = Outfit.objects.all()
    return {'outits': outfits}