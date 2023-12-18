from django.db import models

# Create your models here.

class Task(models.Model):
    task=models.CharField(max_length=200)
    priority=models.CharField(max_length=100)
    date=models.DateField()

class CompletedTask(models.Model):
    completed_task=models.CharField(max_length=200)
    completed_date=models.DateField()
