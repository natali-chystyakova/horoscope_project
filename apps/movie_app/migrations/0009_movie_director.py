# Generated by Django 4.2.4 on 2023-10-05 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("movie_app", "0008_director_remove_movie_director"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="movie_app.director"),
        ),
    ]
