from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="user/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="catalog/index.html"), name="logout"
    ),
    path(
        "register/",
        views.SignUpView.as_view(template_name="user/register.html"),
        name="register",
    ),
]
