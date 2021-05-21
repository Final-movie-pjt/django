from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from movies.models import Movie


# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE )
    content = models.TextField()
    rank = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
