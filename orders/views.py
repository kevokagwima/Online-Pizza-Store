from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import regular_pizza, silican_pizza, subs, toppings, pasta, salads, dinner_platters, order_items, order

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

    if user is None:
        return render(request, "orders/login.html", {"message":"Could not register. Try again"})
    else:
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

@login_required
def add_to_cart(request):
    try:
        products = order_items.objects.all()
    except order_items.DoesNotExist:
        raise Http404("product does not exist")

    context = {
        "product": products,
    }
    return render(request, "orders/order.html", context)
