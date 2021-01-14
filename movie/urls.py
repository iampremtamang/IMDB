from django.urls import path
from . import views

app_name='movie'


urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('category/<str:category>/', views.MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>/', views.MovieLanguage.as_view(), name='movie_language'),
    
]