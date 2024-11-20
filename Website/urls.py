"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

from pages.views import (
    about_view,
    admissions_view,
    api_docs_view,
    campus_view,
    careers_view,
    developers_register_view,
    developers_view,
    error404_view,
    home_view,
    placements_view,
    student_current_sem_chart,
    student_details_chart,
)
from UniWeb import views

urlpatterns = [
    # MOSTLY STATIC PAGES
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("404", error404_view, name="error404"),
    path("about", about_view, name="about_view"),
    path("campus", campus_view, name="campus_view"),
    path("login", views.login_view, name="login_view"),
    path("careers", careers_view, name="careers_view"),
    path("placements", placements_view, name="placements_view"),
    path("admissions", admissions_view, name="admissions_view"),
    path("developers/", developers_view, name="developers_view"),
    path(
        "developers/register", developers_register_view, name="developers_register_view"
    ),
    # DOCS URL
    path("api-docs", api_docs_view, name="api_docs_view"),
    # USER ACTION URLS
    path("user/", include("UniWeb.urls")),
    # REST FRAMEWORK URLS
    path("api-client/", include("UniWeb.api.urls", namespace="api")),
    path("lineChart/<str:user>", student_details_chart, name="student_details_chart"),
    path(
        "student-curr-sem-chart/<str:user>",
        student_current_sem_chart,
        name="student-curr-sem-chart",
    ),
    # ADMIN DASHBOARD
    path("dashboard/", views.dashboard_view, name="dashboard_view"),
    path("dashboard/<str:user>", views.viewuser_admin_view, name="viewuser_view"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
