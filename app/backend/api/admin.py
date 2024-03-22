from django.contrib import admin
from .models import Trip, City


# Register your models here.
@admin.register(Trip)
class AdminTrip(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price_confort",
        "price_econ",
        "city",
        "duration",
        "seat",
        "bed",
    ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]