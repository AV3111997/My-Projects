# Generated by Django 4.2.6 on 2023-11-04 06:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce_app', '0005_rename_type_outfit_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Quantity must be greater than 0.'), django.core.validators.MaxValueValidator(5, 'Quantity must be less than 5.')], verbose_name='Quantity')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Cart',
                'unique_together': {('user', 'product')},
            },
        ),
    ]
