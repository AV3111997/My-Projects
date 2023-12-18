from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name='Name'
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        verbose_name='Slug'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Outfit(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name='Type'
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        verbose_name='Slug'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type)
        super(Outfit, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name='Name'
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        verbose_name='Slug'
    )
    price = models.FloatField(
        default=0,
        verbose_name='Price'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Category'
    )
    outfit = models.ForeignKey(
        Outfit,
        default='',
        on_delete=models.CASCADE,
        verbose_name='Outfit',
    )
    stock = models.IntegerField(
        default=0,
        verbose_name='Stock'
    )
    available = models.BooleanField(
        default=True,
    )
    image = models.ImageField(
        upload_to='products/images/',
        verbose_name='image',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
