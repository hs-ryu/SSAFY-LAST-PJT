from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
# 디렉터랑 액터는 credit으로 받아옴. 얘네 둘은 어차피 한 API로 호출 가능하니까 한번만 할까?
# 가능할까?
class Director(models.Model):
    name = models.CharField(max_length=100)
class Actor(models.Model):
    name = models.CharField(max_length=100)

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    # 상세정보나, 유튜브에서 예고편 들고오려면 id값 필요한듯.
    movie_id = models.IntegerField()
    # genres = models.ManyToManyField(Genre, related_name=movies)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    # directors = models.ManyToManyField(Director)
    # actors = models.ManyToManyField(Actor)
    vote_average = models.FloatField()
    # like_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    netflix = models.TextField(default='')
    watcha = models.TextField(default='')
    wavve = models.TextField(default='')
    naver = models.TextField(default='')
    release_date = models.DateField()
    clicked = models.IntegerField(default=0)
    last_cliked_time = models.DateTimeField(default=timezone.make_aware(datetime.datetime.strptime("2021-05-18 16:30:30", '%Y-%m-%d %H:%M:%S')))


class NowShowingMovie(models.Model):
    movieNm = models.CharField(max_length=100)
    openDt = models.DateField()
    audiAcc = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    # 나중에 DB 초기화 할떄 default 지우고 다시 마이그레이션
    userRating = models.FloatField(default=0)