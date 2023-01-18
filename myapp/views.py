from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import os
from .utils import tmdb_api
from django.contrib.auth.decorators import login_required

def index(request):
  return render(request, 'movies/index.html')

def about(request):
  return render(request, 'movies/about.html')

def contact(request):
  return render(request, 'movies/contact.html')

def search(request):
  query = request.GET.get('query')
  if not query:
    return redirect('myapp:movie_list')
  
  # Search for the movie using the TMDB API
  movies = tmdb_api.search_movies(query)
  
  if not movies:
    messages.error(request, 'No movies found')
    return redirect('myapp:movie_list')
  
  # Redirect to the movie detail page if a single movie is found
  if len(movies) == 1:
    return redirect('myapp:movie_detail', movie_id=movies[0]['id'])
  
  # Otherwise, display a list of movies
  return render(request, 'movies/movie_list.html', {'movies': movies})

#@login_required
def movie_list(request):
  # Get all movies from the TMDB API
  movies, total_pages = tmdb_api.get_all_movies()
  
  return render(request, 'movies/movie_list.html', {
    'movies': movies,
    'total_pages': total_pages,
  })

#@login_required
def movie_detail(request, movie_id):
    api_key = os.getenv("TMDB_API_KEY")
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    trailer_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}&language=en-US"
    download_url = f"https://api.themoviedb.org/3/movie/{movie_id}/download?api_key={api_key}&language=en-US"
    movie_response = requests.get(movie_url)
    trailer_response = requests.get(trailer_url)
    download_response = requests.get(download_url)
    movie = movie_response.json()
    trailer = trailer_response.json()
    download = download_response.json()
    context = {
        "movie": movie,
        "trailer": trailer,
        "download": download,
    }
    return render(request, "movies/movie_detail.html", context)
