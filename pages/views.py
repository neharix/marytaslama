from django.shortcuts import render

from UniWeb.models import *


def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def error404_view(request, *args, **kwargs):
    return render(request, "404.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def campus_view(request, *args, **kwargs):
    campuses = Campus.objects.all()[:3]
    return render(request, "campus.html", {"campuses": campuses})


def admissions_view(request, *args, **kwargs):
    faculty_names = [faculty.name for faculty in Faculty.objects.all()[:3]]
    students_count = [
        [faculty.first_year_students for faculty in Faculty.objects.all()[:3]]
    ]
    students_count.append(
        [faculty.second_year_students for faculty in Faculty.objects.all()[:3]]
    )
    students_count.append(
        [faculty.third_year_students for faculty in Faculty.objects.all()[:3]]
    )
    students_count.append(
        [faculty.fourth_year_students for faculty in Faculty.objects.all()[:3]]
    )
    students_count.append(
        [faculty.fifth_year_students for faculty in Faculty.objects.all()[:3]]
    )
    return render(
        request,
        "admissions.html",
        {"faculty_names": faculty_names, "students_count": students_count},
    )
