from django.views.generic import TemplateView, RedirectView


class BlogListView(TemplateView):
    """
    Simple placeholder view for a list of blog posts
    """
    template_name = "blog/list.html"


class BlogDetailView(TemplateView):
    """
    Simple placeholder view for a detail view of a single post
    """
    template_name = "blog/detail.html"


class PostRedirect(RedirectView):
    url = "/post"
