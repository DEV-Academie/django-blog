from django.views.generic import DetailView, ListView, TemplateView, RedirectView

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"

    def get_queryset(self):
        return Post.objects.filter(published=True).all()


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post


class PostRedirect(RedirectView):
    url = "/post"
