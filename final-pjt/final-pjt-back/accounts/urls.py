from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('<int:user_id>/', views.profile),  # 유저 프로필
    path('my_profile/', views.my_profile),  # 본인 프로필
    path('<int:user_id>/follow/', views.follow, name='follow'), # 팔로우 기능
]
