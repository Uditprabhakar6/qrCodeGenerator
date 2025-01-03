# Generated by Django 5.1.4 on 2024-12-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QrCodeData",
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
                ("is_active", models.BooleanField(default=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated_at"),
                ),
                ("created_by", models.CharField(blank=True, max_length=256, null=True)),
                ("updated_by", models.CharField(blank=True, max_length=256, null=True)),
                ("qr_name", models.CharField(max_length=200)),
                ("qr_cust_data", models.CharField(max_length=500)),
                ("qr_final_data", models.CharField(max_length=1000)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
