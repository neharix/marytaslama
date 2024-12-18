from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from UniWeb.models import *


def home_view(request, *args, **kwargs):
    try:
        context = {"page_data": MainPageContent.objects.all()[0]}
    except:
        context = {}
    return render(request, "index.html", context)


def error404_view(request, *args, **kwargs):
    return render(request, "404.html", {})


def about_view(request, *args, **kwargs):
    try:
        context = {"page_data": AboutPage.objects.all()[0]}
    except:
        context = {}
    return render(request, "about.html", context)


def campus_view(request, *args, **kwargs):
    try:
        context = {"page_data": CampusPage.objects.all()[0]}
    except:
        context = {}

    context["campuses"] = Campus.objects.all()[:3]
    return render(request, "campus.html", context)


def admissions_view(request, *args, **kwargs):
    try:
        context = {"page_data": AdmissionsPage.objects.all()[0]}
    except:
        context = {}
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
    context["faculty_names"] = faculty_names
    context["students_count"] = students_count
    return render(request, "admissions.html", context)
