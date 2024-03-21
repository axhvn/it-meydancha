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


def projects_page(request):
    projects = models.Project.objects.all()
    return render(
        request,
        "pages/projects.html",
        {
            "projects": projects,
        },
    )


def project_detail(request, pk):
    project = models.Project.objects.get(id=pk)
    return render(
        request,
        "pages/project_detail.html",
        {
            "project": project,
        },
    )
