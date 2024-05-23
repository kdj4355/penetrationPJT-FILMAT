from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('review/', views.review_list, name='review_list'), # 전체 리뷰 리스트
    path('movie/<int:movie_pk>/review/', views.movie_review_page, name='movie_review_page'),     # 세부 영화 정보에 달린 리뷰 보기
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'), # 리뷰 디테일
    path('review/<int:review_pk>/like/', views.review_like, name='review_like'),    # 리뷰 좋아요 기능
    path('review/<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),  # 댓글 생성
    path('comments/', views.comment_list, name='comment_list'),  # 게시글에 달린 댓글 리스트
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),    # 댓글 디테일
]
