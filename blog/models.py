from datetime import date

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish_date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.CharField(max_length=200)

    def save(self, *args, **kwargs):

        if self.published and not self.publish_date:
            self.publish_date = date.today()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
