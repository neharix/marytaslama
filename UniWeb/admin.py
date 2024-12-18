from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(MainPageContent)
admin.site.register(AdmissionsPage)
admin.site.register(AboutPage)
admin.site.register(InfoColumn)
admin.site.register(AboutInfoColumn)
admin.site.register(CarouselImage)

admin.site.register(CampusPage)
admin.site.register(CampusFirstInfoColumn)
admin.site.register(CampusSecondInfoColumn)


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
