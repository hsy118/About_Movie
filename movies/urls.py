from django.urls import path

from. import views

app_name = "movies"

urlpatterns = [
    path('', views.popular_movies, name='movie_list'),
    # path('popular/', views.popular_movies, name='popular_moives'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommendation/<str:genre1>/<str:genre2>/', views.recommendation, name='recommendation'),
    path('<str:genre>/', views.show_movies, name='show_movies')
]
