from . import views

# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
