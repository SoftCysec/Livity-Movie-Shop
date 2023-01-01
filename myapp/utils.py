import requests
import os

def get_movies_from_api(page=1):
    api_key = os.environ['TMDB_API_KEY']
    api_url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&page={page}"
    response = requests.get(api_url)
    return response.json()

def get_movie_from_api(movie_id):
    api_key = os.environ['TMDB_API_KEY']
    api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(api_url)
    return response.json()


def search_movies(query, page=1):
    api_key = os.environ['TMDB_API_KEY']
    api_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&page={page}"
    response = requests.get(api_url)
    return response.json()