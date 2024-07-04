from django.urls import path
from .views import PostListView, PostDetailView, CommentView, FollowView, UserView, UserDetailView, LikeDetailView, LikeView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('follows/', FollowView.as_view(), name='follow-list'),
    path('user/', UserView.as_view(), name='follow-list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='follow-list'),
    path('like/', LikeView.as_view(), name='follow-list'),
    path('like/<int:pk>', LikeDetailView.as_view(), name='follow-list'),
]
