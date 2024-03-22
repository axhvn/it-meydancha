from django.urls import path

from . import views

urlpatterns = [
    path("contact/", views.contact_page, name="contact"),
    path("project-detail/<int:pk>/", views.project_detail, name="project_detail"),
    path("projects/", views.projects_page, name="projects"),
    path("about/", views.about_page, name="about"),
    path("", views.home_page, name="home"),
]
