from django.urls import path

from blog.views import (
    AddCommentView,
    BlogDetailView,
    BlogListView,
    PostsPerCategory,
    PostRedirect
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("<int:pk>/comment/", AddCommentView.as_view(), name="add_comment"),
    # path("", BlogDetailView.as_view(), name="detail-2"),
    path("categorie/<slug:slug>/", PostsPerCategory.as_view(), name="category"),
    path("redirect/", PostRedirect.as_view(), name="redirect"),
]
