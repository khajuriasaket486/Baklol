from django.db import models
from authorapp.models import AuthorModel
from datetime import datetime


class VideoModel(models.Model):
    heading = models.CharField(max_length=200)
    video_link = models.URLField()
    author = models.ForeignKey(AuthorModel, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.heading
