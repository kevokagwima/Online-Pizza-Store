from django.urls import path

from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("home", views.index, name="index"),
    path("registration", views.registration, name="registration"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
