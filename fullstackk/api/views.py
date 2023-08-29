from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from .forms import NameForm


def display_form(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            u = form.save(
                commit=False
            )  # here commit=false to save it later after password hashing
            username = form.cleaned_data["username"]
            # first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # print(username, "\n", first_name, ",", last_name)
            u.set_password("password")  # password hashing done
            u.save(comm)  # now commit
            return display_copy(request)

    else:
        form = NameForm()
    return render(request, "api/index.html", {"form": form})


def display_copy(request):
    context = {}

    return render(request, "api/index_copy.html", context)
