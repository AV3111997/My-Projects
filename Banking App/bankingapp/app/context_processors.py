from .models import District

def district_branch(request):
    branch = District.objects.all()
    return {'district_branch': branch}
