from django.db import models
from django.contrib.auth.models import User
from ecommerce_app.models import Product
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Cart(models.Model):

    class Meta:
        verbose_name_plural = "Cart"
        unique_together = ['user', 'product']

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product',
    )

    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1,
        validators=[
            MinValueValidator(1, "Quantity must be greater than 0."),
            MaxValueValidator(5, "Quantity must be less than 5."),
        ]
    )

    totalcost = models.IntegerField(
        verbose_name='Total Cost',
        default=0
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On',
    )
