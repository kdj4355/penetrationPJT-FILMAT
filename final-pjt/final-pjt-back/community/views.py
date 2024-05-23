from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from movies.models import Movie

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from django.views.decorators.http import require_safe
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer, MovieSerializer
from .models import Review, Comment


# 리뷰 리스트
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def review_list(request):
    # 리뷰 리스트 받아오기
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    # 리뷰 생성
    elif request.method == 'POST':
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 세부 리뷰 페이지 나만 볼 수 있음.
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    # 세부 리뷰 보기
    if request.method == 'GET':
    
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    # 리뷰 삭제
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
    # 리뷰 수정하기
    elif request.method == 'PUT':
        # partial=True 추가 - 요소하나만 수정할 수도 있기 때문
        serializer = ReviewSerializer(review, data=request.data, partial=True)

        if request.user == review.user:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

# 세부 영화 페이지에 달린 리뷰 보기
@api_view(['GET'])
def movie_review_page(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 리뷰 좋아요 구현
@api_view(['POST'])
def review_like(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        liked = False
    else:
        review.like_users.add(user)
        liked = True

    like_count = review.like_users.count()
    liked_data = {
        'liked': liked,
        'liked_count': like_count,
    }
    return Response(liked_data, status.HTTP_200_OK)


# 댓글 생성
@api_view(['POST'])
def create_comment(request, review_pk):
    user = request.user
    # print(user)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 댓글 조회
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 세부 댓글 조회 수정 삭제
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 세부 댓글 정보
    if request.method == 'GET':     
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # 댓글 삭제
    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    # 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            if request.user == comment.user:
                serializer.save()
                return Response(serializer.data)
