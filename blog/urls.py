from django.urls import path

from blog.views import (
    BlogDetailView,
    BlogListView,
    PostsPerCategory,
    PostRedirect
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    # path("", BlogDetailView.as_view(), name="detail-2"),
    path("categorie/<slug:slug>/", PostsPerCategory.as_view(), name="category"),
    path("redirect/", PostRedirect.as_view(), name="redirect"),
]
