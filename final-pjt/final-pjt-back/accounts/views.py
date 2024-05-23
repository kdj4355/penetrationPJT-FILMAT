from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User
from .serializers import UserSerializer
from movies.models import Movie

# 유저 프로필
@api_view(['GET'])
def profile(request, user_id):
    # 유저 정보 가져오기
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
@api_view(['GET', 'PUT'])
def my_profile(request):
    # 본인 프로필
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # 프로필 수정
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 팔로우 기능 구현
@api_view(['POST', 'DELETE'])
def follow(request, user_id):
    user = request.user
    person = get_object_or_404(User, pk=user_id)

    # 팔로우
    if request.method == 'POST':
        if user != person:
            if user in person.followers.all():
                person.followers.add(user)
                return Response(status=status.HTTP_200_OK)
            # 유저가 없다면 404 에러코드
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
    # 언팔로우
    elif request.method == 'DELETE':
        if user in person.followers.all():
            person.followers.remove(user)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
    

