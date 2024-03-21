from django.shortcuts import render


def home_page(request):
    return render(request, "pages/home.html")


def about_page(request):
    return render(request, "pages/about.html")
