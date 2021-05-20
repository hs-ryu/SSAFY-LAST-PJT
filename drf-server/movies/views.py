

from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer

# Create your views here.

import requests
from justwatch import JustWatch
import datetime
from django.utils import timezone

from movies import serializers


# 중요한것 하나. API로 영화 정보들을 불러와서 json 파일에 저장할때,
# model이라는 필드를 추가해 우리가 정의한 모델 이름과 같도록 만들기 (ex- "model":"movies.genre" 이러면 장르 모델로 저장이 됨.)
# fields는 오리가 정의한 모델의 테이블 이름에 맞게 들어가야함

'''ex
"fields": {
    "title" : "~~~~"
    "release_data" : ~~~,
    "overview" : ~~~,
    "genres" : [
        1,
        2,
        3
    ]
} 
'''


# api를 사용해서 영화 데이터 불러와서 저장하기. 일단 샘플로만 만들기
def savemovies(request):
    # 전체 영화 (test : TMDB top rated 20개)
    just_watch = JustWatch(country = 'KR')
    for i in range(1,6):
        TMDB_API_KEY = '0ca69f265e9245060dace2ea98e1e056'
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}'
        response = requests.get(URL).json()
        get_movies = response['results']
        for get_movie in get_movies:
            movie = Movie()
            movie.title = get_movie['title']
            movie.movie_id = get_movie['id']
            movie.overview = get_movie['overview']
            movie.poster_path = get_movie['poster_path']
            movie.vote_average = get_movie['vote_average']
            movie.release_date = get_movie['release_date']
            # movie.save()
            try:
                results = just_watch.search_for_item(query=f"{movie.title}")['items'][0]['offers']
                for result in results:
                    url = result['urls']['standard_web']
                    if 'watcha' in url:
                        movie.watcha = url
                    elif 'netflix' in url:
                        movie.netflix = url
                    elif 'wavve' in url:
                        movie.wavve = url
                    elif 'naver' in url:
                        movie.naver = url
                # movie.save()
            except:
                pass
            finally:
                movie.save()
    return render(request, 'movies/savemovies.html')


# 전체 영화 정보 조회
@api_view(['GET'])
def getmovies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 개별 영화 상세 정보 조회
@api_view(['GET'])
def getmoviedetail(request, movie_pk):
    now_time = timezone.make_aware(datetime.datetime.now())
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 일단 확인을 위해 minute으로 
    if datetime.datetime.now().minute > movie.last_cliked_time.minute:
        movie.last_cliked_time = now_time
        movie.clicked = 0
        movie.save()
    movie.clicked += 1
    movie.last_cliked_time = now_time
    movie.save()
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 인기 영화 정보 조회
# 여기 clicked 사용
@api_view(['GET'])
def getpopularmovies(request):
    now_time = timezone.make_aware(datetime.datetime.now())
    movies = get_list_or_404(Movie)
    # 다 0이면 뭘로 들고올까? 랜덤?
    recommend_movies = Movie.objects.order_by('-clicked')[:10]
    for movie in movies:
        if datetime.datetime.now().minute > movie.last_cliked_time.minute:
            movie.last_cliked_time = now_time
            movie.clicked = 0
            movie.save()
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getnowshowing(request):
    # 두 날짜의 차이가 44일
    movies = Movie.objects.filter(release_date__gte = datetime.datetime.now()-datetime.timedelta(days=44))
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)