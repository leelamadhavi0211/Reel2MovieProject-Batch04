from fastapi import APIRouter
from services.tmdb_services import get_tmdb_movie_details

router = APIRouter()


@router.get("/fetch-movies")
def fetch_movies(movie: str):
    return get_tmdb_movie_details(movie)