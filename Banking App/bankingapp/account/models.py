from django.db import models
from app.models import District, Branch
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    GENDER_CHOICES = [
        ('', 'Specify your gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    ACCOUNT_CHOICES = [
        ('', 'Choose account type'),
        ('Savings', 'Savings Account'),
        ('Checking', 'Checking Account'),
        ('Other', 'Other Account Type'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20)
    materials_provide = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
