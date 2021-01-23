from django.db import models
from authorapp.models import AuthorModel
from datetime import datetime


class MemeModel(models.Model):
    heading = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    author = models.ForeignKey(AuthorModel, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.heading

