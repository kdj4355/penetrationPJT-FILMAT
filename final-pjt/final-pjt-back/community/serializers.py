from rest_framework import serializers
from .models import Review, Comment
from accounts.models import User
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.contrib.auth import get_user_model

# 전체 리뷰 리스트
class ReviewListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# 리뷰에 댓글 정보
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', )

# 리뷰 세부정보
class ReviewSerializer(serializers.ModelSerializer):    
    class ReviewUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = '__all__'
        
    user = ReviewUserSerializer(read_only=True)
    

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
      
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', )

# 영화 디테일 페이지에 달린 리뷰
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
