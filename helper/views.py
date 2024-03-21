from django.shortcuts import render

from . import models


def home_page(request):
    projects = models.Project.objects.all().order_by("-id")[:2]
    return render(
        request,
        "pages/home.html",
        {
            "projects": projects,
        },
    )


def about_page(request):
    return render(
        request,
        "pages/about.html",
    )
