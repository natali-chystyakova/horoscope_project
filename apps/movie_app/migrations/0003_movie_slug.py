# Generated by Django 4.2.4 on 2023-09-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie_app", "0002_movie_budget_movie_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
