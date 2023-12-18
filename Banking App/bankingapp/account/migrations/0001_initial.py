# Generated by Django 5.0 on 2023-12-12 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("Savings", "Savings Account"),
                            ("Checking", "Checking Account"),
                            ("Other", "Other Account Type"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "materials_provided",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.branch"
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.district"
                    ),
                ),
            ],
        ),
    ]
