from django.db import models
from datetime import datetime
from authorapp.models import AuthorModel


class ArticleModel(models.Model):
    genre = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_on_carousel = models.BooleanField(default=False)
    author = models.ForeignKey(AuthorModel, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.heading