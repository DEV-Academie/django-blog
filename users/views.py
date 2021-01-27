from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm


class Login(LoginView):
    template_name = "auth/login.html"


class RegisterView(CreateView):
    model = get_user_model()
    form_class = RegisterForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("user")
