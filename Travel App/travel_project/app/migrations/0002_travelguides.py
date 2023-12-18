# Generated by Django 4.2.5 on 2023-12-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TravelGuides",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("designation", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="packages/images/")),
            ],
        ),
    ]
