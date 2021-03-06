from datetime import date

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.CharField(max_length=200)
    category = models.ForeignKey("blog.Category",
                                 on_delete=models.PROTECT,
                                 related_name="posts",
                                 null=True,
                                 blank=True,
                                 )

    class Meta:
        verbose_name = "Bericht"
        verbose_name_plural = "Berichten"

    def save(self, *args, **kwargs):

        if self.published and not self.publish_date:
            self.publish_date = date.today()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.id})"


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categorieën"

    def __str__(self):
        return f"{self.title} ({self.posts.count()})"


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE, related_name="comments")
    is_approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reactie"
        verbose_name_plural = "Reacties"

    def __str__(self):
        return f"Reactie door {self.user.username} bij {self.post} ({self.date})"
