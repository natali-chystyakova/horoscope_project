from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ["name", "rating", "year", "budget"]
#
# # Register your models here.
# admin.site.register(Movie, MovieAdmin)

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ["floor", "number", "actor"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ["name", "rating"]  #поля отображать
    # exclude = ["slug"]  # поля исключить
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["budget"]  # нельзя менять, только чтение
    list_display = ["name", "rating", "director", "currency", "budget", "rating_status"]
    list_editable = ["rating", "director", "currency", "budget"]  # что можно редактировать
    ordering = ["rating"]  # сортиорвка в админке
    list_per_page = 10  # пагинация в админке
    actions = ["set_dollars", "set_euro"]  # регистрируем действие
    search_fields = ["name__istartswith", "rating"]  # поиск
    filter_horizontal = ["actors"]

    @admin.display(ordering="rating", description="Статус")
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return "Зачем это смотреть"
        if mov.rating < 70:
            return "Разок можно глянуть"
        if mov.rating <= 85:
            return "Зачет"
        return "Топчик"

    @admin.action(description="Установить валюту в доллар")
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description="Установить валюту в евро")
    def set_euro(self, request, queryset: QuerySet):
        count_updated = queryset.update(currency=Movie.EURO)
        self.message_user(
            request,
            f"Было обновлено {count_updated}",
            messages.ERROR,  # сообщение будет красного цвета (по умолчанию - зеленое INFO)
        )
