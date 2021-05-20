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