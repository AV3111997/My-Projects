# Generated by Django 4.2.6 on 2023-11-02 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_product_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250, unique=True, verbose_name='Type')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='outfit',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.outfit', verbose_name='Outfit'),
        ),
    ]