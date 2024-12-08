from django.contrib import admin

from .models import *


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ["name", "capacity"]
    readonly_fields = ("id",)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "first_year_students",
        "second_year_students",
        "third_year_students",
        "fourth_year_students",
        "fifth_year_students",
    ]
