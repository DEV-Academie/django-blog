from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import Login, RegisterView
from blog.views import LoggedInUserCommentsView, DeleteCommentView


urlpatterns = [
    path("inloggen/", Login.as_view(), name="login"),
    path("uitloggen/", LogoutView.as_view(), name="logout"),
    path("registreer/", RegisterView.as_view(), name="register"),
    path("comments/", LoggedInUserCommentsView.as_view(), name="user_comments"),
    path("comments/delete/<int:pk>/", DeleteCommentView.as_view(), name="delete_comment")
]
