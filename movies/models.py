from django.db import models
from django.db.models.base import Model

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=100)
    # movies = models.ManyToManyField(Movie)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    released_date = models.TextField()
    poster_path = models.CharField(max_length=300)
    genres = models.ManyToManyField(Genre)
