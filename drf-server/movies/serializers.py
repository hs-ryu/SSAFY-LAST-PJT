from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Comment, Movie, NowShowingMovie, Review

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'movie_id', 'poster_path', 'clicked',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','movie_id', 'overview', 'poster_path', 'vote_average', 'netflix', 'watcha', 'wavve', 'naver', 'clicked','release_date', )

class NowShowingMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowShowingMovie
        fields = ('movieNm', 'openDt', 'audiAcc', 'image_path')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'rank','created_at', 'updated_at',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content','title', 'rank','created_at', 'updated_at',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at')