from .models import Movie, Genre
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame


def recommend():
    movies = Movie.objects.all()
    df = read_frame(movies)
    # 영화 장르 리스트 불러오기
    g_list = []
    for movie in movies:
        m_g =[]
        genres = movie.genres.all()
        # 각 영화의 분류된 장르들을 g_list에 담고
        for genre in genres:
            m_g.append(genre.genre_name)
        g_list+=[m_g]
    g_list = [[" ".join(x)] for x in g_list]


    # 장르 리스트 데이터프레임 형태로 변경
    gdf = pd.DataFrame({'g_list':g_list})
    # 기존의 영화 데이터와 합치기
    movie_data = pd.concat([df, gdf], axis=1)
    # 장르 전처리
    movie_data['g_list'] = movie_data['g_list'].apply(lambda x: " ".join(x))
    #g_list = np.array(g_list)
    # 각 장르들의 문자열 값을 숫자로 벡터화
    count_vector = CountVectorizer(ngram_range=(1,3))
    c_vector_genre = count_vector.fit_transform(movie_data['g_list'])
    # 장르의 consine similarity를 구한 벡터 값을 구함
    genre_c_sim = cosine_similarity(c_vector_genre, c_vector_genre).argsort()[:,::-1]

    def get_recommend_movie(df, movie_title, top=20):
        target_movie_index = df[df['title'] == movie_title].index.values
        # cosine similarity 중 해당 값과 비슷한 cosine similarity 20개를 구함
        sim_index = genre_c_sim[target_movie_index, : top].reshape(-1)
        # 이름이 같은 영화는 제외
        sim_index = sim_index[sim_index != target_movie_index]

        result = df.iloc[sim_index].sort_values('vote_count', ascending=False)[:5]
        result = result[['id', 'title']]
        return result
    for movie in movies:
        title = movie.title
        try:
            rc_mv = get_recommend_movie(movie_data, title)
            for movie_id in rc_mv['id']:
                m = Movie.objects.get(pk=movie_id)
                movie.recommend_movies.add(m)
        except ValueError:
            continue