from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.projects_page, name="projects"),
    path("about/", views.about_page, name="about"),
    path("", views.home_page, name="home"),
]
