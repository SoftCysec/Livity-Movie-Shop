from django.shortcuts import render
from django.core.paginator import Paginator
from .utils import get_movies_from_api, get_movie_from_api, search_movies

def index(request):
    return render(request, 'movies/index.html')

def about(request):
    return render(request, 'movies/about.html')

def contact(request):
    return render(request, 'movies/contact.html')

def search(request):
    query = request.GET.get('query')
    movies = search_movies(query)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/search_results.html', context)

def movie_list(request):
    try:
        page = int(request.GET.get('page'))
    except (TypeError, ValueError):
        page = 1
    movies = get_movies_from_api(page)
    paginator = Paginator(movies['results'], 20)
    movies = paginator.page(page)
    context = {
        'movies': movies,
        'previous_page': movies.number - 1,
        'next_page': movies.number + 1,
    }
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_movie_from_api(movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/movie_detail.html', context)
