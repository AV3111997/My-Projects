# Generated by Django 5.0 on 2023-12-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_account_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="account",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
