from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('savemovies/', views.savemovies, name='savemovies'),
    path('getmovies/', views.getmovies, name='getmovies'),
    path('getmovies/<int:movie_pk>/', views.getmoviedetail, name='getmoviedetail'),
    path('getpopularmovies/', views.getpopularmovies, name='getpopularmovies'),
    path('getnowshowing/', views.getnowshowing, name='getnowshowing'),
]