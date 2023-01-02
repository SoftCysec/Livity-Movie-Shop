from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact'),
  path('movies/', views.movie_list, name='movie_list'),
  path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
  path('search/', views.search, name='search'),
]
