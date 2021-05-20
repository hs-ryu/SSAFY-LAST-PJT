from django.db import models
from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'movie_id', 'poster_path', 'clicked',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','movie_id', 'overview', 'poster_path', 'vote_average', 'netflix', 'watcha', 'wavve', 'naver', 'clicked','release_date', )
