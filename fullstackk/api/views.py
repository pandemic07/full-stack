from django.shortcuts import render
from .models import User


def display(request):
    listt = User.objects.all()
    context = {
        "users_list": "Here are your Users:",
        "listt": listt,
    }

    return render(request, "api/index.html", context)


def display_copy(request):
    listt = User.objects.all()
    context = {}

    return render(request, "api/index_copy.html", context)
