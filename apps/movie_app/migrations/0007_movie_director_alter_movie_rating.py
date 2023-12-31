# Generated by Django 4.2.4 on 2023-10-03 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie_app", "0006_alter_movie_currency"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="director",
            field=models.CharField(default="Квентин Тарантино", max_length=100),
        ),
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]
            ),
        ),
    ]
