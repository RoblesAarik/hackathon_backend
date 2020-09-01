import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Business


# Home route
def index(request):
    if request.method == "GET":
        return HttpResponseRedirect(reverse('index'))

# Register


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Check that passwords match
        if password != confirmation:
            return render(request, "mysite/register.html", {
                "message": "Try again there, bud"
            })

        # Attempt to create a new user
        try:
            user = User.objects.create_user(email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "mysite/register.html", {
                "message": "Email is already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "mysite/register.html")


# login
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication was successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "mysite/login.html", {
                "message": "Invalid email or password"
            })
    if request.method == "GET":
        return render(request, "mysite/login.html")

# Logout


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# about us


def about_us(request):
    if request.method == "GET":
        return HttpResponseRedirect(reverse("about_us"))
