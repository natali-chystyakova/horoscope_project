from django.urls import path
from . import views

app_name = "movie_app"

urlpatterns = [
    path("", views.show_all_movie, name="movies"),
    path("<int:id_movie>", views.show_one_movie, name="movie_detail"),
    path("directors", views.show_all_directors, name="directors"),
    path("directors/<int:id_director>", views.show_one_director, name="director_detail"),
    path("actors", views.show_all_actors, name="actors"),
    path("actors/<int:id_actor>", views.show_one_actor, name="actor_detail"),
]
