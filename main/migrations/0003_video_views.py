# Generated by Django 5.0.6 on 2024-07-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_customuser_video_delete_articles"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
