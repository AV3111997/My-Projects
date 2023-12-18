from django import forms
from django.contrib.auth.models import User
from .models import Account, Branch, District
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, EmailValidator


class ApplicationForm(forms.ModelForm):
    name_validator = RegexValidator(
        regex=r'^[A-Za-z\s]+$',
        message='Enter a valid name.',
        code='invalid_name'
    )

    age_validator = [
        MinValueValidator(18, message='You must be at least 18 years old.'),
        MaxValueValidator(100, message='Age cannot exceed 100 years.')
    ]

    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Enter a valid phone number.',
        code='invalid_phone'
    )

    email_validator = EmailValidator(message='Enter a valid email address.')

    # Form Fields
    name = forms.CharField(
        validators=[name_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    age = forms.IntegerField(
        validators=age_validator,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    gender = forms.ChoiceField(
        choices=Account.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #fff;'})
    )

    phone_number = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        validators=[email_validator],
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #fff;'})
    )

    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #fff;'})
    )

    account_type = forms.ChoiceField(
        choices=Account.ACCOUNT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #fff;'})
    )

    class Meta:
        model = Account
        fields = ['name', 'date_of_birth', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'account_type']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.is_bound:
            self.fields['branch'].queryset = Branch.objects.none()