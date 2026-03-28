""" 
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.connection import embeddings_collection
from datetime import datetime

router = APIRouter(prefix="/api", tags=["embeddings"])

class EmbeddingData(BaseModel):
    movie_name: str
    embeddings: list

@router.post("/store-embeddings")
async def store_embeddings(data: EmbeddingData):
    
    try:
        if not data.movie_name or not data.embeddings:
            raise HTTPException(status_code=400, detail="movie_name and embeddings are required")
        
        result = embeddings_collection.update_one(
            {"movie_name": data.movie_name},
            {"$set": {
                "movie_name": data.movie_name,
                "embeddings": data.embeddings,
                "updated_at": datetime.now()
            }},
            upsert=True
        )
        
        return {
            "status": "success",
            "message": f"Stored {len(data.embeddings)} embeddings for {data.movie_name}",
            "matched": result.matched_count,
            "upserted": result.upserted_id if result.upserted_id else "updated"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/embeddings-status")
async def embeddings_status():
   
    try:
        count = embeddings_collection.count_documents({})
        movies = embeddings_collection.find({}, {"movie_name": 1})
        movie_names = [m.get("movie_name", "Unknown") for m in movies]
        
        return {
            "total_movies": count,
            "movies": movie_names
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import logging
from database.connection import embeddings_collection

router = APIRouter()
logger = logging.getLogger("uvicorn.error")

class EmbeddingRequest(BaseModel):
    movie_name: str
    embeddings: List[List[float]] # Must be a list of lists containing floats

@router.post("/upload-embeddings")
async def upload_embeddings(data: EmbeddingRequest):
    try:
        # Convert Pydantic model to a plain dictionary for MongoDB
        payload = {
            "movie_name": data.movie_name,
            "embeddings": data.embeddings
        }
        
        result = embeddings_collection.update_one(
            {"movie_name": data.movie_name},
            {"$set": payload},
            upsert=True
        )
        return {"status": "success", "action": "upserted" if result.upserted_id else "updated"}
        
    except Exception as e:
        # This will print the EXACT error in your FastAPI terminal
        logger.error(f"DATABASE CRASH: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
