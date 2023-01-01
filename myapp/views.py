from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/movie_list.html', context)

def index(request):
    return render(request, 'movies/index.html', {})

def about(request):
    return render(request, 'movies/about.html', {})

def contact(request):
    return render(request, 'movies/contact.html', {})
