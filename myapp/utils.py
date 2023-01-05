import requests
import os

# TMDB API configuration
TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
TMDB_API_URL = 'https://api.themoviedb.org/3'

class TmdbApi:
  def search_movies(self, query):
    """Searches for movies using the TMDB API."""
    params = {
      'api_key': TMDB_API_KEY,
      'query': query,
    }
    r = requests.get(f'{TMDB_API_URL}/search/movie', params=params)
    if r.status_code == 200:
      return r.json()['results']
    return []

  def get_all_movies(self, page=1):
    """Gets all movies from the TMDB API."""
    params = {
      'api_key': TMDB_API_KEY,
      'page': page,
    }
    r = requests.get(f'{TMDB_API_URL}/discover/movie', params=params)
    if r.status_code == 200:
      data = r.json()
      return data['results'], data['total_pages']
    return [], 0

  def get_popular_movies(self, page=1):
    """Gets the popular movies from the TMDB API."""
    params = {
      'api_key': TMDB_API_KEY,
      'page': page,
    }
    r = requests.get(f'{TMDB_API_URL}/movie/popular', params=params)
    if r.status_code == 200:
      data = r.json()
      return data['results'], data['total_pages']
    return [], 0

  def get_movie(self, movie_id):
    """Gets the details of a movie from the TMDB API."""
    params = {
      'api_key': TMDB_API_KEY,
    }
    r = requests.get(f'{TMDB_API_URL}/movie/{movie_id}', params=params)
    if r.status_code == 200:
      return r.json()
    return {}

# Create a singleton instance of the TmdbApi class
tmdb_api = TmdbApi()
