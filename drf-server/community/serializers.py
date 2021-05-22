from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'categories')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user')


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    class Meta:
        model = Article
        # 게시글-댓글 사이에 1:N 관계가 형성되었을때 'comment_set'를 넣어주면 조회했을때 같이 나옴.
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comment_count', 'categories')