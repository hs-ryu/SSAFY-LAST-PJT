

from django.http import response
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, NowShowingMovie, Genre, Review, Comment, Vote, VoteComment
from .serializers import MovieListSerializer, MovieSerializer, NowShowingMovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer, VoteListSerializer, VoteSerializer

# Create your views here.

import requests
from justwatch import JustWatch
import datetime
from django.utils import timezone


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# 중요한것 하나. API로 영화 정보들을 불러와서 json 파일에 저장할때,
# model이라는 필드를 추가해 우리가 정의한 모델 이름과 같도록 만들기 (ex- "model":"movies.genre" 이러면 장르 모델로 저장이 됨.)
# fields는 우리가 정의한 모델의 테이블 이름에 맞게 들어가야함


# 관리자만 가능하게
# from django.contrib.admin.views.decorators import staff_member_required
# @staff_member_required
# 혹은
# @permission_required('is_staff')
# 체크 해봐야함.

def savegenre(request):
    TMDB_API_KEY = '0ca69f265e9245060dace2ea98e1e056'
    URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR'
    response = requests.get(URL).json()
    get_genres = response['genres']
    for get_genre in get_genres:
        genre = Genre()
        genre.id = get_genre['id']
        genre.name = get_genre['name']
        genre.save()
    return render(request, 'movies/savemovies.html')



# api를 사용해서 영화 데이터 불러와서 저장하기. 일단 샘플로만 만들기
def savemovies(request):
    # 전체 영화 (test : TMDB top rated 20개)
    just_watch = JustWatch(country = 'KR')
    # 19페이지오류
    for i in range(1,3):
        TMDB_API_KEY = '0ca69f265e9245060dace2ea98e1e056'
        URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KR&page={i}'
        response = requests.get(URL).json()
        get_movies = response['results']
        for get_movie in get_movies:
            try:
                if get_movie['release_date'] and get_movie['title'] and get_movie['id'] and get_movie['overview'] and get_movie['poster_path'] and get_movie['vote_average'] and get_movie['genre_ids']:
                    movie = Movie()
                    movie.release_date = get_movie['release_date']
                    movie.title = get_movie['title']
                    movie.movie_id = get_movie['id']
                    movie.overview = get_movie['overview']
                    movie.poster_path = get_movie['poster_path']
                    movie.vote_average = get_movie['vote_average']
                    genres = get_movie['genre_ids']
                    movie.save()
            except:
                continue
            for genre in genres:
                targets = Genre.objects.filter(id=genre)
                movie.genres.add(targets[0])
            # 있는것만 DB에 넣자.
            # movie.save()
            try:
                results = just_watch.search_for_item(query=f"{movie.title}")['items']
                if len(results) > 1:
                    for result in results:
                        if (movie.title == result['title']) and (movie.release_date[:4] == str(result['original_release_year'])):
                            urls_info = result['offers']
                            for url_info in urls_info:
                                url = url_info['urls']['standard_web']
                                if 'watcha' in url:
                                    movie.watcha = url
                                elif 'netflix' in url:
                                    movie.netflix = url
                                elif 'wavve' in url:
                                    movie.wavve = url
                                elif 'naver' in url:
                                    movie.naver = url
                else:
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


def savenowshowing(request):
    KOBIS_API_KEY = '351749075a99330b8e539beb9afaf302'
    yesterday = datetime.datetime.now()- datetime.timedelta(days=2)
    year = yesterday.strftime("%Y")
    month = yesterday.strftime("%m")
    day = yesterday.strftime("%d")
    today = year + month + day
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={KOBIS_API_KEY}&targetDt={today}'
    response = requests.get(URL).json()
    get_movies = response['boxOfficeResult']['dailyBoxOfficeList']
    ClientID = 'k35V4NgZQkjVVQAZ8FtS'
    ClientSecret = 'w1d2eYndo3'
    for get_movie in get_movies:
        movie = NowShowingMovie()
        movie.movieNm = get_movie['movieNm']
        movie.openDt = get_movie['openDt']
        movie.audiAcc = get_movie['audiAcc']
        NAVER_URL = f'https://openapi.naver.com/v1/search/movie.json?query={movie.movieNm}'
        NAVER_response = requests.get(NAVER_URL,headers={"X-Naver-Client-Id":ClientID,"X-Naver-Client-Secret":ClientSecret}).json()
        # print(NAVER_response)
        movie.image_path = NAVER_response['items'][0]['image']
        movie.userRating = NAVER_response['items'][0]['userRating']
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
    # if (datetime.datetime.now().hour > movie.last_cliked_time.hour) or (datetime.datetime.now().day > movie.last_cliked_time.day) or (datetime.datetime.now().month > movie.last_cliked_time.month) or (datetime.datetime.now().year > movie.last_cliked_time.year)
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
        # if (datetime.datetime.now().hour > movie.last_cliked_time.hour) or (datetime.datetime.now().day > movie.last_cliked_time.day) or (datetime.datetime.now().month > movie.last_cliked_time.month) or (datetime.datetime.now().year > movie.last_cliked_time.year)
        if datetime.datetime.now().minute > movie.last_cliked_time.minute:
            movie.last_cliked_time = now_time
            movie.clicked = 0
            movie.save()
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getnowshowing(request):
    movies = get_list_or_404(NowShowingMovie)
    serializer = NowShowingMovieSerializer(movies, many=True)
    return Response(serializer.data)

    # # 두 날짜의 차이가 44일
    # movies = Movie.objects.filter(release_date__gte = datetime.datetime.now()-datetime.timedelta(days=44))
    # serializer = MovieListSerializer(movies, many=True)
    # return Response(serializer.data)

# 해당 영화의 전체 리뷰 조회
@api_view(['GET'])
def getallreviews(request, movie_pk):
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

# 상세 리뷰 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def getreview(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

# 해당 영화에 리뷰 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def createreview(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 여기서 영화 유저 평점을 계산해서 다시 집어넣는 로직 필요.
        movie.rank_total += float(request.data['rank'])
        reviews = Review.objects.filter(movie_id=movie_pk)
        movie.rank_average = movie.rank_total / (len(reviews) + 1)
        movie.save()
        serializer.save(movie=movie, user=request.user)
        # 나중에 유저 기능 구현하면 아래껄로
        # serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def deletereview(request, movie_pk, review_pk):
    # 해당 review를 작성한 유저가 아니라면 삭제하지 못함.
    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    # 리뷰를 삭제했을때 리뷰가 없다면 그 영화의 유저 평점을 0으로 만드는 로직 필요
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.rank_total -= review.rank
    reviews = Review.objects.filter(movie_id=movie_pk)
    if len(reviews)-1:
        movie.rank_average = movie.rank_total / (len(reviews) - 1)
    else:
        movie.rank_average = 0
    movie.save()
    review.delete()
    return Response({'id': review_pk})


# 리뷰 수정
@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def updatereview(request, movie_pk, review_pk):
    # 해당 review를 작성한 유저가 아니라면 수정하지 못함.
    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    reviews = Review.objects.filter(movie_id=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.rank_total -= review.rank
    movie.rank_total += float(request.data['rank'])
    movie.rank_average = movie.rank_total / (len(reviews))
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
        movie.save()
        serializer.save()
        return Response(serializer.data)

# 리뷰의 댓글 작성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def createcomment(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review = review, user=request.user)
        return Response(serializer.data)

# 리뷰의 댓글 불러오기
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def getcomments(request, movie_pk, review_pk):
    comments = Comment.objects.filter(review_id=review_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 리뷰의 댓글 삭제하기
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def deletecomment(request, movie_pk, review_pk, comment_pk):
    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response({ 'id': comment_pk })

# 리뷰의 댓글 수정하기
@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def updatecomment(request, movie_pk, review_pk, comment_pk):
    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


# # 투표 전부 조회
# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def getallvotes(request, movie_pk):
#     votes = Vote.objects.filter(movie_id=movie_pk)
#     serializer = VoteListSerializer(votes, many=True)
#     return Response(serializer.data)

# #투표 상세
# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def getvote(requet, movie_pk, vote_pk):
#     vote = get_object_or_404(Vote, pk=vote_pk)
#     serializer = VoteSerializer(vote)
#     return Response(serializer.data)


# #투표 생성
# @api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def createvote(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = VoteSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(movie = movie)
#         return Response(serializer.data)

# # 투표 삭제
# @api_view(['DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def deletevote(request, movie_pk, vote_pk):
#     vote = get_object_or_404(Vote, pk=vote_pk)
#     vote.delete()
#     return Response({ 'id': vote_pk})


# # 투표 댓글 생성, 조회

