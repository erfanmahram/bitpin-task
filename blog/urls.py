from django.urls import path
from .views import PostListView, RatePostView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/rate/', RatePostView.as_view(), name='rate-post'),
]
