from django import forms
from . models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'priority', 'date']
        
    task = forms.CharField(
        label='Task',
        widget=forms.TextInput(attrs={'class': 'custom-css-class'}),
    )
    
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    priority = forms.ChoiceField(
        label='Priority',
        choices=PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'custom-css-class'}),
    )
    
    date = forms.DateField(
        label='Date',
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
    )