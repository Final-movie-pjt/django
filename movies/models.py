from django.db import models

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
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    recommend_movies = models.ManyToManyField('self', symmetrical=False, related_name = 'recommended')