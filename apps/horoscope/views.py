from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from django.views.generic import TemplateView
from django.urls import reverse
from datetime import datetime


class HoroscopeView(TemplateView):
    template_name = "horoscope/horoscope.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Horoscope"
        # context["sign"] = sign_zodiac
        return context


zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": " Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
}

zodiac_dates = {
    "aries": ((3, 21), (4, 19)),
    "taurus": ((4, 20), (5, 20)),
    "gemini": ((5, 21), (6, 20)),
    "cancer": ((6, 21), (7, 22)),
    "leo": ((7, 23), (8, 22)),
    "virgo": ((8, 23), (9, 22)),
    "libra": ((9, 23), (10, 22)),
    "scorpio": ((10, 23), (11, 21)),
    "sagittarius": ((11, 22), (12, 21)),
    "capricorn": ((12, 22), (1, 19)),
    "aquarius": ((1, 20), (2, 18)),
    "pisces": ((2, 19), (3, 20)),
}


types = {
    "fire": ["aries", "leo", "sagittarius"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"],
    "water": ["cancer", "scorpio", "pisces"],
}


def sign_elem(request):
    zodiacs = list(zodiac_dict)
    context = {
        "zodiacs": zodiacs,
        "zodiac_dict": zodiac_dict,
    }
    return render(request, "horoscope/index_zodiac.html", context=context)


def type_elem(request):
    zodiacs_types = list(types)
    li_elements_type = ""
    for type_z in zodiacs_types:
        redirect_path_type = reverse("horoscope:horoscope_type_n", args=[type_z])
        li_elements_type += f"<li> <a href='{redirect_path_type}' > {type_z.title()} </a> </li>"
    response_t = f"""
    <ul>
        {li_elements_type}
    </ul>
    """
    return HttpResponse(response_t)


def get_info_about_sing_zodiac(request, sign_zodiac: str):
    # description = zodiac_dict.get(sign_zodiac)
    # if description := zodiac_dict.get(sign_zodiac):
    #     response = render_to_string("horoscope/horoscope.html")
    #     return HttpResponse(response)
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        "description_zodiac": description,
        "sign": sign_zodiac,
        "sign_name": description.split()[0],
        "zodiacs": zodiacs,
    }
    return render(request, "horoscope/horoscope.html", context=data)


def get_info_about_sing_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неверный порядковый номер знака зодивка {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope:horoscope_str", args=[name_zodiac])
    # return HttpResponseRedirect(f"/horoscope/{name_zodiac}")
    return HttpResponseRedirect(redirect_url)


def get_info_about_type_zodiac(request, type_z: str):
    # description = zodiac_dict.get(sign_zodiac)
    if description_t := types.get(type_z):
        return HttpResponse(description_t)
    else:
        return HttpResponseNotFound(f"неизвестный тип зодиака {type_z}")


def get_info_by_date(request, month, day):
    try:
        date_obj = datetime(month=month, day=day, year=2000)
        # Год можно выбрать любой, так как нам важен только день и месяц
        for sign, (start_date, end_date) in zodiac_dates.items():
            start_month, start_day = start_date
            end_month, end_day = end_date
            start_obj = datetime(month=start_month, day=start_day, year=2000)
            end_obj = datetime(month=end_month, day=end_day, year=2000)
            if start_obj <= date_obj <= end_obj:
                return HttpResponse(sign)
            else:
                HttpResponseNotFound("Неизвестный")
    except ValueError:
        return HttpResponseNotFound("неверная дата")
