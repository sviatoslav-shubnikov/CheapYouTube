# Generated by Django 5.0.6 on 2024-07-05 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articles",
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
                (
                    "title",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(20)],
                        verbose_name="title",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(upload_to="static/main/photo/", verbose_name="photo"),
                ),
                (
                    "video",
                    models.FileField(upload_to="static/main/video/", verbose_name="video"),
                ),
            ],
        ),
    ]
