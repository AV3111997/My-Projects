from .models import TravelGuides

def tour_guides(request):
    guides = TravelGuides.objects.all() 
    return {'guides': guides}
