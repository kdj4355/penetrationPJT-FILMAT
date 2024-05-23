from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import GenreListSerializer, MovieListSerializer, MovieSerializer, ActorListSerializer, ActorSerializer, UserSelectGenreSerializer
from .models import Movie, Genre, Actor

# 장르 목록 가져오기
@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    if request.method == 'GET':
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 장르 좋아요 구현
@api_view(['POST'])
def genre_like(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    user = request.user
    if genre.like_users.filter(pk=user.pk).exists():
        genre.like_users.remove(user)
    else:
        genre.like_users.add(user)
    return Response(status=status.HTTP_200_OK)

# 영화 목록 가져오기
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)[:500]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 영화 세부사항
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 영화 좋아요 구현
@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked =True
    
    # 좋아요 수 계산
    like_count = movie.like_users.count()
    like_data = {
        'liked': liked,
        'liked_count': like_count,
    }

    return Response(like_data, status.HTTP_200_OK)

# 영화 인기도에 따라 20개 추출
@api_view(['GET'])
def movie_popularity(request):
    movies = Movie.objects.all().order_by('-popularity')[:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 평점이 높은 영화 20개 추출
@api_view(['GET'])
def vote_average(request):
    movies = Movie.objects.all().order_by('-vote_average')[:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 영화 추천 서비스
@api_view(['GET'])
def recommended(request):
    user = request.user
    
    # 사용자의 선호장르와 배우를 가져옴
    like_genres = user.like_genres.all()
    like_actors = user.like_actors.all()
    
    # 선호 장르에 속하는 영화 목록을 가져옴
    genre_movies = Movie.objects.filter(genres__in=like_genres).distinct()
    
    # 선호 배우가 출연한 선호 장르의 영화를 필터링
    actor_genre_movies = genre_movies.filter(movie_actor__in=like_actors).distinct()
    
    # 선호 배우가 출연한 영화가 있으면 이를 추천 목록으로 사용
    if actor_genre_movies.exists():
        recommended_movies = actor_genre_movies.order_by('-popularity')
    # 아니면 영화를 인기도 순으로 정렬하고 
    else:
        recommended_movies = genre_movies.order_by('-popularity')

        # 추천 목록이 10개 이상이면 평점순으로 다시 정렬합니다.
        if len(recommended_movies) >= 10:
            recommended_movies = recommended_movies.order_by('-vote_average')

    # 10개 미만이면 선호 장르에서 인기도가 높은 영화로 채움
    if recommended_movies.count() < 10:
        additional_movies = genre_movies.exclude(id__in=recommended_movies).order_by('-popularity')
        recommended_movies = list(recommended_movies) + list(additional_movies[:10 - recommended_movies.count()])
    else:
        recommended_movies = recommended_movies[:10]

    serializer = MovieSerializer(recommended_movies, many=True)
    return Response(serializer.data)

# 배우 목록 가져오기
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Actor)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 배우 세부사항
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 배우 좋아요 저장
@api_view(['POST'])
def actor_like(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    user = request.user
    if actor.like_users.filter(pk=user.pk).exists():
        actor.like_users.remove(user)
        liked = False
    else:
        actor.like_users.add(user)
        liked =True
    
    # 좋아요 수 계산
    like_count = actor.like_users.count()
    like_data = {
        'liked': liked,
        'liked_count': like_count,
    }

    return Response(like_data, status.HTTP_200_OK)

