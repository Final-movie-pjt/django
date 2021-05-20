from django.shortcuts import render
from .models import Movie, Genre
from .makeDB import makeDB

isDbUploaded = False

# Create your views here.
def index(request):
    global isDbUploaded
    if not isDbUploaded:
        makeDB()
        isDbUploaded = True
    return render(request, 'movies/index.html')