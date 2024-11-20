from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def error404_view(request, *args, **kwargs):
    return render(request, "404.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def campus_view(request, *args, **kwargs):
    return render(request, "campus.html", {})


def admissions_view(request, *args, **kwargs):
    return render(request, "admissions.html", {})
