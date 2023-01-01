from django.shortcuts import render
from .models import Movie

import requests

def movie_list(request):
    api_key = 'ed224da74c443beeb88f1d204fe4e7a0'
    api_url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
    response = requests.get(api_url)
    movies = response.json()['results']
    return render(request, 'movies/movie_list.html', {'movies': movies})


def index(request):
    return render(request, 'movies/index.html', {})

def about(request):
    return render(request, 'movies/about.html', {})

def contact(request):
    return render(request, 'movies/contact.html', {})
