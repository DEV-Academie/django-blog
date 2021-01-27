from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, RedirectView
from django.views.generic.detail import SingleObjectMixin

from blog.forms import CommentForm
from blog.models import Category, Comment, Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/list.html"

    def get_queryset(self):
        return Post.objects.filter(published=True).all()


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post

    def get_object(self, queryset=None):
        prefetch = Prefetch(
            "comments",
            queryset=Comment.objects.filter(is_approved=True),
            to_attr="approved_comments"
        )
        post = Post.objects.prefetch_related(prefetch).get(pk=self.kwargs.get("pk"))

        return post


class PostsPerCategory(DetailView):
    model = Category
    template_name = "blog/category.html"


class AddCommentView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/add_comment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class HandleFormView(SingleObjectMixin, FormView):
    template_name = "blog/add_comment.html"
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        data = form.cleaned_data

        comment = Comment(
            comment=data["comment"],
            user=self.request.user,
            post=self.object
        )

        comment.save()
        return HttpResponseRedirect(reverse_lazy("detail", kwargs={"pk": self.object.pk}))


# class AddCommentViewAlternative(LoginRequiredMixin, FormView):
#     template_name = "blog/add_comment.html"
#     form_class = CommentForm
#     blog_post = None
#
#     def dispatch(self, request, *args, **kwargs):
#         try:
#             self.blog_post = Post.objects.get(pk=self.kwargs.get("pk"))
#         except Post.DoesNotExist:
#             raise Http404("Bericht bestaat niet")
#
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post"] = self.blog_post
#         return context
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#
#         comment = Comment(
#             comment=data["comment"],
#             user=self.request.user,
#             post=self.blog_post
#         )
#
#         comment.save()
#         return HttpResponseRedirect(reverse_lazy("detail", kwargs={"pk": self.blog_post.pk}))


class PostRedirect(RedirectView):
    url = "/post"
