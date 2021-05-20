from django.db import models
from django.db.models.base import Model

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=100)
    # movies = models.ManyToManyField(Movie)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    # released_date = models.TextField()
    released_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    poster_path = models.CharField(max_length=300, null=True)
    genres = models.ManyToManyField(Genre)
