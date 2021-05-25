from django.db import models
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Movie, Genre
from community.models import Review
from .makeDB import makeDB
from .recommendation import recommend as reco
from chat.models import Room
import random

# Create your views here.
def index(request):
    # 장르 데이터
    genre_data = Genre.objects.all()

    # 채팅방 목록 가져오기
    rooms = Room.objects.filter(count_users__lte=0)
    for room in rooms:
        room.delete()
    rooms = Room.objects.all()

    # 추천 영화 5개 아무거나 랜덤으로 제시
    genre_index = random.randrange(0, len(genre_data))
    genre_id = genre_data[genre_index].genre_id
    g = Genre.objects.get(genre_id=genre_id)
    recommend_movies = g.movie_set.all()[:6]

    context = {
        'genre_data': genre_data,
        'rooms': rooms,
        'recommend_movies': recommend_movies,
    }

    return render(request, 'movies/index.html', context)

def get_api(request):
    makeDB()
    return redirect('movies:index')

def get_movies(request, genre_id):
    # 장르 아이디와 일치하는 영화를 가져오기
    g = Genre.objects.get(genre_id=genre_id)
    movies = g.movie_set.all()
    context = {
        'movies': movies,
        'genre': g,
    }
    return render(request, 'movies/genre.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    reviews = movie.review_set.all()
    context = {
        'movie' : movie,
        'reviews': reviews,
    }
    return render(request, 'movies/detail.html', context)


def recommend(request):
    reco()
    return redirect('movies:index')

def search(request):
    search_word = request.GET['search-word']
    if search_word:
        movie_list = Movie.objects.filter(Q(title__icontains=search_word) | Q(overview__icontains=search_word)).distinct()
        message = ''
        error = ''

        if len(movie_list) == 0:
            genres = Genre.objects.all()
            genre_index = random.randrange(0, len(genres))
            genre_id = genres[genre_index].genre_id
            g = Genre.objects.get(genre_id=genre_id)
            movie_list = g.movie_set.all()
            error = '에 해당하는 영화가 없습니다'
            message = '이런 영화는 어떠세요?'

        context = {
            'search_word': search_word,
            'movie_list': movie_list,
            'message': message,
            'error': error,
        }

        return render(request, 'movies/search.html', context)

