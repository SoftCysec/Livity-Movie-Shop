import tmdbv3api
import os

from myapp.models import Movie

# Load the TMDB API key from an environment variable
api_key = os.environ['TMDB_API_KEY']

# Create an API client using the API key
api_client = tmdbv3api.TMDb()
api_client.api_key = api_key

# Fetch a list of movies
movies = api_client.Movies().latest()

# Iterate through the list of movies and add them to the database
for movie in movies:
    new_movie = Movie(
        title=movie.title,
        year=movie.release_date.year,
        poster_image=movie.poster_path,
        plot_summary=movie.overview
    )
    new_movie.save()
