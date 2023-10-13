from django.urls import path
from . import views

app_name = "horoscope"

urlpatterns = [
    # path("<sign_zodiac>", views.HoroscopeView.as_view(), name="horoscope"),
    path("", views.sign_elem, name="horoscope"),
    path("<int:month>/<int:day>", views.get_info_by_date, name="horoscope_date"),
    path("type/", views.type_elem, name="horoscope_type"),
    path("type/<str:type_z>", views.get_info_about_type_zodiac, name="horoscope_type_n"),
    path("", views.HoroscopeView.as_view(), name="horoscope"),
    # path("<sign_zodiac>", views.LeoView.as_view(), name="horoscope"),
    path("<int:sign_zodiac>", views.get_info_about_sing_zodiac_by_number, name="horoscope_n"),
    path("<str:sign_zodiac>", views.get_info_about_sing_zodiac, name="horoscope_str"),
]
