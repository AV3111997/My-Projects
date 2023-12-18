# Generated by Django 4.2.6 on 2023-11-01 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.category', verbose_name='Category')),
            ],
        ),
    ]
