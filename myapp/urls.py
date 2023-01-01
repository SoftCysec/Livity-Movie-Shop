from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movie_detail/', views.movie_list, name='movie_detail'),
    path('search_results/', views.movie_list, name='search'),
]
