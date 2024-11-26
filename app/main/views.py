from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict[str, str] = {"title": "ii-constructor - главная"}

    return render(request, "main/index.html", context)


def documentation(request) -> HttpResponse:
    context: dict[str, str] = {"title": "ii-constructor - документация"}

    return render(request, "main/documentation.html", context)
