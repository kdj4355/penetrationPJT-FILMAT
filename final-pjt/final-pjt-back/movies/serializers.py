from rest_framework import serializers
from .models import Movie, Genre, Actor
from django.contrib.auth import get_user_model
from community.models import Review


# 장르 리스트
class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# 영화 리스트
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# 영화 세부정보
class MovieSerializer(serializers.ModelSerializer):
    class ReviewSerializer(serializers.ModelSerializer):    
        class ReviewUserSerializer(serializers.ModelSerializer):
                class Meta:
                    model = get_user_model()
                    fields = '__all__'
            
        user = ReviewUserSerializer(read_only=True)                
        
        class Meta:
            model = Review
            fields = '__all__'
            read_only_fields = ('user', )
    reviews = ReviewSerializer(many=True, read_only=True)


    class MovieActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
    actors = MovieActorListSerializer(source='movie_actor', many=True, read_only=True)   
    
    class MovieGenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    movie_genres = MovieGenreListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

# 배우 리스트
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 배우 세부정보
class ActorSerializer(serializers.ModelSerializer):
    # 영화 정보 역참조
    movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'

# 영화 추천 사이트
# 사용자가 선택한 장르별 영화
class UserSelectGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('like_genres', 'like_actors', )
