from django.urls import path
from . import views

urlpatterns = [    
    path("genre/", views.genre_list),   # 장르 리스트
    path("genre/<int:genre_pk>/like/", views.genre_like),   # 장르 좋아요
    path("movie_list/", views.movie_list), # 전체 영화 리스트
    path("movie_list/<int:movie_pk>/", views.movie_detail), # 세부 영화 페이지
    path("movie_list/<int:movie_pk>/like/", views.movie_like), # 영화 좋아요
    path('movie_list/popularity/', views.movie_popularity),
    path('movie_list/vote_average/', views.vote_average),
    path("actor/", views.actor_list),
    path("actor/<int:actor_pk>/", views.actor_detail),
    path("actor/<int:actor_pk>/like/", views.actor_like),
    path("recommended/", views.recommended), # 유저별로 영화 추천 페이지
]
