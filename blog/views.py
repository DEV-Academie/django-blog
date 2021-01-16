from django.views.generic import DetailView, ListView, RedirectView

from blog.models import Category, Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"

    def get_queryset(self):
        return Post.objects.filter(published=True).all()


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post


class PostsPerCategory(DetailView):
    model = Category
    template_name = "blog/category.html"

class PostRedirect(RedirectView):
    url = "/post"
