from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import jwt


@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    # 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 팔로우
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    target_person = get_object_or_404(get_user_model(), pk=user_pk)
    request_person = request.user

    if target_person != request_person:
        if target_person.followers.filter(pk=request_person.pk).exists():
            target_person.followers.remove(request_person)
            followed = False
        else:
            target_person.followers.add(request_person)
            followed = True
    follow_status = {
        'followed' : followed,
        'followersCount' : target_person.followers.count(),
        'followingsCount' : target_person.followings.count(),
    }
    return JsonResponse(follow_status)


@api_view(['POST'])
def verify_user(request):
    decoded = jwt.decode(request.data.get('token'), 'settings.py의 SECRET_KEY', algorithms=["HS256"])
    user_id = decoded.get('user_id')
    username = decoded.get('username')
    you = get_object_or_404(get_user_model(), pk=user_id)
    superuser_status = True if you.is_superuser else False
    user_info = {
        'username': username,
        'user_id': user_id,
        'issuperuser': superuser_status,
    }
    return JsonResponse(user_info)