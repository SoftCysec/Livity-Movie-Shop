# Livity-Movie-Shop
Livity is a web application for buying and renting the latest movies from your favorite actors and directors.

## Features
- Browse a selection of popular movies
- Search for movies by title or actor
- Purchase or rent movies online
- Leave reviews and ratings for movies
## Requirements
- Python 3.7 or higher
- Django 3.1 or higher
- TMDB API key (sign up at https://www.themoviedb.org/)
## Installation
1. Clone the repository:
```
git clone https://github.com/SoftCysec/livity-movie-shop.git
```
2. Navigate to the project directory:
```
cd livity-movie-shop
```
3. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
5. Set the TMDB API key as an environment variable:
```
export TMDB_API_KEY='your_api_key_goes_here'
```
6. Run the migrations:
```
python manage.py migrate
```
7. Run the development server:
```
python manage.py runserver
```
The app will be available at http://127.0.0.1:8000/.

## Contributing
We welcome contributions to Livity-Movie-Shop! If you would like to report a bug or request a feature, please open an issue. If you would like to submit a patch, please fork the repository and submit a pull request.

## License
Livity-Movie-Shop is licensed under the MIT License. See the LICENSE file for more details.
