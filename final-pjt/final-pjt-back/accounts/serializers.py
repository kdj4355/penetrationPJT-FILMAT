from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from allauth.account.adapter import get_adapter

from .models import User
from django.contrib.auth import get_user_model
from movies.models import Genre, Actor, Movie
from community.models import Review, Comment
from community.serializers import ReviewSerializer
from movies.serializers import ActorSerializer

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
    )
    email = serializers.EmailField(
        required=False,
    )

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'email': self.validated_data.get('email', ''),
        }
    
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.set_password(self.cleaned_data.get('password1'))
        user.nickname = self.cleaned_data.get('nickname')
        user.email = self.cleaned_data.get('email')
        user.save()
        adapter.save_user(request, user, self)
        return user

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, ''):
            extra_fields.append('nickname')
        
            
        model = UserModel
        fields = ('pk', *extra_fields)

# 각각 user의 세부 정보 가져오기
class UserSerializer(serializers.ModelSerializer):


    # 좋아하는 영화 가져오기
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    # 좋아하는 배우 가져오기
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
    
    # 좋아하는 장르 가져오기
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    like_genres = GenreSerializer(many=True, read_only=True)
    like_actors = ActorSerializer(many=True, read_only=True) 
    like_movies = MovieSerializer(many=True, source='like_moives', read_only=True)

    reviews = ReviewSerializer(many=True, source='review_set', read_only=True)

    # 유저의 팔로잉한 데이터 가져오기
    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'nickname')
    followings = FollowingSerializer(many=True, read_only=True)

    # 유저의 팔로워를 데이터 가져오기
    class FollowerSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'nickname')
    followers = FollowerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'