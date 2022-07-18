from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    NotificationListView,
    temp,
)
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name = 'home'),
    path('home/',PostListView.as_view(),name = 'home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post_detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post_delete'),
    path('post/new/',PostCreateView.as_view(),name = 'post_create'),
    path('notification/',NotificationListView.as_view(),name = 'notification'),
    path('get-notification/',temp,name = 'temp'),
]
