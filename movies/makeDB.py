from .models import Movie, Genre
import requests
from .env import TMDB_API_KEY


def makeDB():
    API_KEY = TMDB_API_KEY
    GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'
    POPULAR_MOVIE_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page='
    
    # with open('movies\genres.json') as json_file:
    #     genre_data = json.load(json_file)['genres']

    # 장르에 데이터 추가
    genre_data = requests.get(GENRE_URL).json()['genres']
    for data in genre_data:
        Genre.objects.create(genre_id=data['id'], genre_name=data['name'])

    # 영화에 데이터 추가
    # 20 페이지까지의 영화 넣기
    # with open('movies\movie.json', 'r', encoding="utf-8") as json_file:
    #     movie_data = json.load(json_file)['results']
    for num in range(1, 21):
        url = POPULAR_MOVIE_URL + str(num)
        movie_data = requests.get(url).json()['results']

        for movie in movie_data:
            title = movie.get('title')
            overview = movie.get('overview')
            released_date =  movie.get('release_date')
            poster_path = movie.get('poster_path')
            genre_ids = movie.get('genre_ids')
            vote_average = movie.get('vote_average')
            vote_count = movie.get('vote_count')
            if title and overview and released_date and poster_path and genre_ids and vote_average and vote_count:
                m = Movie.objects.create(title=title, overview=overview, released_date=released_date, poster_path=poster_path, vote_average=vote_average, vote_count=vote_count)
                # 중개 테이블에 데이터 넣기
                for genre in genre_ids:
                    g = Genre.objects.get(genre_id=genre)
                    m.genres.add(g)