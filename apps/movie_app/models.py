from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name} "

    def get_url(self):
        return reverse("movie_app:director_detail", args=[self.id])


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"{self.floor} {self.number}"


class Actor(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDERS = [
        (MALE, "Мужчина"),
        (FEMALE, "Женщина"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актер {self.first_name}  {self.last_name} "
        return f"Актриса {self.first_name}  {self.last_name} "

    def get_url(self):
        return reverse("movie_app:actor_detail", args=[self.id])


class Movie(models.Model):
    EURO = "EUR"
    USD = "USD"
    RUB = "RUB"
    CURRENCY_CHOICES = [
        (EURO, "Euro"),
        (USD, "Dollars"),
        (RUB, "Rubles"),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default="", null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse("movie_app:movie_detail", args=[self.id])

    def __str__(self):
        return f"{self.name} - {self.rating} %"


# python manage.py shell_plus --print-sql
# from apps.movie_app.models import Movie
