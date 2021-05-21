from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # DB 생성과 관련된 URL
    path('savegenre/', views.savegenre, name='savegenre'),
    path('savemovies/', views.savemovies, name='savemovies'),
    path('savenowshowing/', views.savenowshowing, name='savenowshowing'),

    # 영화와 관련된 URL
    path('getmovies/', views.getmovies, name='getmovies'),
    path('getmovies/<int:movie_pk>/', views.getmoviedetail, name='getmoviedetail'),
    path('getpopularmovies/', views.getpopularmovies, name='getpopularmovies'),
    path('getnowshowing/', views.getnowshowing, name='getnowshowing'),

    # 리뷰와 관련된 URL
    path('<int:movie_pk>/reviews/', views.getallreviews, name='getallreviews'),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.getreview, name='getreview'),
    path('<int:movie_pk>/createreview/', views.createreview, name='createreview'),
    path('<int:movie_pk>/reviews/<int:review_pk>/updatereview/', views.updatereview, name='updatereview'),
    path('<int:movie_pk>/reviews/<int:review_pk>/deletereview/', views.deletereview, name='deletereview'),
]