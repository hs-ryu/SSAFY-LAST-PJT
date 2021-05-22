from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Comment, Movie, NowShowingMovie, Review, Vote, VoteComment

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'movie_id', 'poster_path', 'clicked',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','movie_id', 'overview', 'poster_path', 'vote_average', 'netflix', 'watcha', 'wavve', 'naver', 'clicked','release_date', 'trailer')

class NowShowingMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowShowingMovie
        fields = ('movieNm', 'openDt', 'audiAcc', 'image_path')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'rank','created_at', 'updated_at',)

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = ('id', 'content','title', 'rank','created_at', 'updated_at', 'like_users', 'username')
        read_only_fields = ('like_users',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at',)


class VoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('title', 'movie', 'option_one_count', 'option_two_count', 'option_one', 'option_two')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('title', 'option_one_count', 'option_two_count', )

class VoteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteComment
        fields = ('choice', 'content',)