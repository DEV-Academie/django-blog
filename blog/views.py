from django.views.generic import ListView, TemplateView, RedirectView

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"


class BlogDetailView(TemplateView):
    """
    Simple placeholder view for a detail view of a single post
    """
    template_name = "blog/detail.html"


class PostRedirect(RedirectView):
    url = "/post"
