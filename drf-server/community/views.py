from community import serializers
from community.models import Article, Comment
from community.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.shortcuts import get_object_or_404, render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# 게시글 생성
@api_view(['POST'])
def createarticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 모든 게시글 조회
@api_view(['GET'])
def getallarticles(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

# 게시글 상세 조회
@api_view(['GET'])
def getarticle(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

# 게시글 수정
@api_view(['PUT'])
def updatearticle(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
# 게시글 삭제
@api_view(['DELETE'])
def deletearticle(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response({'id' : article_pk})

# 게시글의 댓글 생성
@api_view(['POST'])
def createcomment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article) # 이 시점에 어떤 게시글에 달린 댓글인지에 대한 정보를 추가해줘야함.
        return Response(serializer.data)

# 게시글의 댓글들 조회
@api_view(['GET'])
def getallcomments(reqeust, article_pk):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 게시글의 댓글 수정
@api_view(['PUT'])
def updatecomment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 게시글의 댓글 삭제
@api_view(['DELETE'])
def deletecomment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response({'id' : comment_pk})