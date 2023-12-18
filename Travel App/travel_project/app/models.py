from django.db import models

# Create your models here.

class TravelPackage(models.Model):
    destination_name = models.CharField(max_length=50)
    duration = models.IntegerField()
    persons = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='packages/images/')

    def __str__(self):
        return self.destination_name
    
class TravelGuides(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='packages/images/')

    def __str__(self):
        return self.name

