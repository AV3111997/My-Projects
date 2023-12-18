from django import forms
from . models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'stock', 'image']
        widgets = {
        }
    
    def save(self, commit=True):
        product = super().save(commit=False)
        product.slug = self.cleaned_data['name'].lower().replace(" ", "-")
        if commit:
            product.save()
        return product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {}
        
    def save(self, commit=True):
        category = super().save(commit=False)
        category.slug = self.cleaned_data['name'].lower().replace(" ", "-")
        if commit:
            category.save()
        return category
