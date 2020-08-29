from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField(max_length=264)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
