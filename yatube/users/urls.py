from . import views

# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
    # :TODO add template for fogot password
    path(
        "password_reset_form/", PasswordResetView.as_view(), name="password_reset_form"
    ),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
]
