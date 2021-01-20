from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import Login

urlpatterns = [
    path("inloggen/", Login.as_view(), name="login"),
    path("uitloggen/", LogoutView.as_view(), name="logout"),
]
