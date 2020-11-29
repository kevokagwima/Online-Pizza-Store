from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import Http404, HttpResponse

from .models import dinner_platters, regular_pizza, silican_pizza, subs, toppings, pasta, salads

def register(request):
    if request.method == "GET":
        return render(request, "orders/register.html")

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message":None})
    context = {
        "user": request.user,
        "toppings": toppings.objects.all(),
        "pasta": pasta.objects.all(),
        "salads": salads.objects.all(),
        "regular": regular_pizza.objects.all(),
        "silican": silican_pizza.objects.all(),
        "subs": subs.objects.all(),
        "dinner": dinner_platters.objects.all()
    }
    return render(request, "orders/menu.html", context)

def registration(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    
    user = User.objects.create_user(username, email, password)

    context = {
        "user": user
    }
    return render(request, "orders/login.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message":"Invalid Credentials"})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message":"logged out"})
