from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
