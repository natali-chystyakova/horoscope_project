from django.shortcuts import render, get_object_or_404
from django.db.models import F, Max, Min, Avg
from apps.movie_app.models import Movie, Director, Actor


# Create your views here.
def show_all_movie(request):
    movies = Movie.objects.order_by(F("year").asc(nulls_last=True), "-rating")
    agg = movies.aggregate(Avg("budget"), Max("rating"), Min("rating"))
    return render(request, "movie_app/all_movies.html", {"movies": movies, "agg": agg, "total": movies.count()})


def show_all_directors(request):
    directors = Director.objects.order_by("last_name")

    return render(request, "movie_app/all_directors.html", {"directors": directors, "total": directors.count()})


def show_all_actors(request):
    actors = Actor.objects.order_by("last_name")

    return render(request, "movie_app/all_actors.html", {"actors": actors, "total": actors.count()})


def show_one_movie(request, id_movie: int):
    # movie = Movie.objects.get(id=id_movie)
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, "movie_app/one_movie.html", {"movie": movie})


def show_one_director(request, id_director: int):
    # movie = Movie.objects.get(id=id_movie)
    director = get_object_or_404(Director, id=id_director)
    return render(request, "movie_app/one_director.html", {"director": director})


def show_one_actor(request, id_actor: int):
    # movie = Movie.objects.get(id=id_movie)
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, "movie_app/one_actor.html", {"actor": actor})
