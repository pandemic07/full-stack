from django.shortcuts import render
from .models import User


def display(request):
    listt = User.objects.all()
    context = {
        "users_list": "Here are your Users:",
        "listt": listt,
    }

    return render(request, "api/index.html", context)
