from django.urls import path
from .views import MovieList, MovieDetail, TheaterList, TheaterDetail, ShowtimeList, ShowtimeDetail

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('theaters/', TheaterList.as_view(), name='theater-list'),
    path('theaters/<int:pk>/', TheaterDetail.as_view(), name='theater-detail'),
    path('showtimes/', ShowtimeList.as_view(), name='showtime-list'),
    path('showtimes/<int:pk>/', ShowtimeDetail.as_view(), name='showtime-detail'),
]
