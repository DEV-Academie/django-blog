from django.urls import path

from blog.views import BlogDetailView, BlogListView, PostRedirect

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    # path("", BlogDetailView.as_view(), name="detail-2"),
    path("redirect/", PostRedirect.as_view(), name="redirect"),
]
