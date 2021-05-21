from django.shortcuts import redirect, render
from .models import Movie, Genre
from .makeDB import makeDB

# Create your views here.
def index(request):
    genre_data = Genre.objects.all()
    context = {
        'genre_data': genre_data,
    }
    return render(request, 'movies/index.html', context)

def init(request):
    makeDB()
    return redirect('movies:index')

def get_movies(request, genre_id):
    # 장르 아이디와 일치하는 영화를 가져오기
    g = Genre.objects.get(genre_id=genre_id)
    movies = g.movie_set.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/genre.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)
