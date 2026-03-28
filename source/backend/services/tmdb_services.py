"""
import requests
from database.connection import movies_collection

TMDB_API_KEY = "c033896e9fcf3544f254dc5d26fe36b6"


def fetch_and_store_movies():

    urls = [

         # 🎬 Telugu movies
        f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_original_language=te",
        
        # 🌍 Global popular
        f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}",

        # 🇮🇳 Indian movies
        f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&region=IN",

       

        # 🔥 Top rated
        f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}"
    ]

    count = 0

    for url in urls:

        response = requests.get(url)
        data = response.json()

        for movie in data.get("results", []):

            movie_data = {
                "name": movie["title"],
                "genre": "Unknown",
                "poster": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get("poster_path") else None
            }

            if not movies_collection.find_one({"name": movie["title"]}):
                movies_collection.insert_one(movie_data)
                count += 1

    return {"message": f"{count} movies added"}
    """
import requests
import os

TMDB_API_KEY = "c033896e9fcf3544f254dc5d26fe36b6"
BASE_URL = "https://api.themoviedb.org/3"

def get_tmdb_movie_details(movie_name):
    # 1. Search for the movie to get its TMDB ID
    search_url = f"{BASE_URL}/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": movie_name}
    print(f"DEBUG: Calling TMDB with URL: {search_url}?query={movie_name}")
    search_response = requests.get(search_url, params=params).json()
    results = search_response.get("results", [])

    if not results:
        return None

    # Get the first/most relevant result
    movie_id = results[0]["id"]

    # 2. Get full details using the ID
    details_url = f"{BASE_URL}/movie/{movie_id}"
    details_response = requests.get(details_url, params={"api_key": TMDB_API_KEY}).json()

    return {
        "title": details_response.get("title"),
        "overview": details_response.get("overview"),
        "release_date": details_response.get("release_date"),
        "genres": [g["name"] for g in details_response.get("genres", [])],
       # "poster_path": f"https://image.tmdb.org{details_response.get('poster_path')}",
       "poster": f"https://image.tmdb.org/t/p/w500{details_response.get('poster_path')}" if details_response.get("poster_path") else None,
        "vote_average": details_response.get("vote_average")
    }
