from django.urls import path
from . import views

app_name = "cinema"

urlpatterns = [
    path('movies/', views.MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('movies/<int:pk>/', views.MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='movie-detail'),
    path('genres/', views.GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genre-list'),
    path('actors/', views.ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor-list'),
    path('cinema_halls/', views.CinemaHallViewSet.as_view({'get': 'list', 'post': 'create'}), name='cinema-hall-list'),
]
