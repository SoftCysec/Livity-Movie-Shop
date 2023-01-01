import requests

def get_movie_poster(movie_id):
    # Make a request to the TMDb API for the specified movie
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    api_key = 'your_api_key_goes_here'
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract the poster path from the response
    poster_path = data['poster_path']

    # Build the full poster URL
    poster_url = f'https://image.tmdb.org/t/p/w500{poster_path}'

    return poster_url
