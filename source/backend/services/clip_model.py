"""import numpy as np
from services.embedding_service import get_frame_embedding
from database.connection import embeddings_collection
from services.tmdb_services import get_tmdb_movie_details
from sklearn.metrics.pairwise import cosine_similarity

def predict_movie_from_frames(frame_paths):
    # Fetch all movies from the new 'embeddings' collection
    movies = list(embeddings_collection.find())

    if not movies:
        print("DEBUG: No documents found in embeddings_collection")
        return {"movie": "No dataset", "confidence": 0}

    best_result = {"movie": "Unknown", "confidence": 0}

    for frame in frame_paths:
        # 1. Get embedding and ensure it is 1D or 2D (not 3D)
        input_emb = get_frame_embedding(frame)
        
        # Force input_emb to be exactly (1, 512) or (1, 768)
        input_emb = np.array(input_emb).reshape(1, -1)
       
        for movie in movies:
            movie_name = movie.get("movie_name", "Unknown Movie")
            movie_embeddings = movie.get("embeddings", [])
            
            if not movie_embeddings:
                continue

            # 2. Convert database list to numpy array
            db_embs = np.array(movie_embeddings)

            # 3. Ensure DB embeddings are 2D (Samples, Features)
            if db_embs.ndim == 3:
                db_embs = db_embs.reshape(db_embs.shape[0], -1)
            elif db_embs.ndim == 1:
                db_embs = db_embs.reshape(1, -1)

            # 4. Calculate similarity (Now guaranteed to be 2D vs 2D)
            similarities = cosine_similarity(input_emb, db_embs)
            max_sim = np.max(similarities)

            # Update best result if this is the highest confidence seen so far
            if max_sim > best_result["confidence"]:
                best_result = {
                    "movie": movie_name,
                    "confidence": round(float(max_sim), 3)
                }
            
            print(f"Checking {movie_name}: Current Sim: {max_sim:.3f} | Best: {best_result['confidence']}")

    # Final threshold check
    if best_result["confidence"] < 0.3:
        return {
            "movie": "Unknown",
            "confidence": best_result["confidence"]
        }

    final_result = best_result

    if final_result["movie"] != "Unknown":
        tmdb_data = get_tmdb_movie_details(final_result["movie"])
        if tmdb_data:
            # Merge AI confidence with TMDB details
            final_result.update(tmdb_data)

    return final_result
"""
import numpy as np
from services.embedding_service import get_frame_embedding
from database.connection import embeddings_collection
from services.tmdb_services import get_tmdb_movie_details
from sklearn.metrics.pairwise import cosine_similarity

def check_compatibility(input_emb, db_embs):
    # input_emb shape: (1, 512)
    # db_embs shape: (N, 512)
    if input_emb.shape[1] != db_embs.shape[1]:
        print(f"CRITICAL: Dimension Mismatch! Query: {input_emb.shape[1]}, DB: {db_embs.shape[1]}")
        return False
    return True

# Dimensions for common CLIP models:
# openai/clip-vit-base-patch32 -> 512
# openai/clip-vit-large-patch14 -> 768

def predict_movie_from_frames(frame_paths):
    # 1. Load all movie data once to avoid DB hits inside loops
    movies = list(embeddings_collection.find())
    if not movies:
        return {"movie": "No dataset", "confidence": 0}

    best_overall_sim = -1.0
    best_movie_name = "Unknown"

    # 2. Process each frame
    for frame in frame_paths:
        input_emb = get_frame_embedding(frame)
        # Ensure it's 2D: (1, 512)
        input_emb = np.array(input_emb).reshape(1, -1)

        for movie in movies:
            movie_name = movie.get("movie_name", "Unknown")
            movie_embeddings = movie.get("embeddings", [])
            
            if not movie_embeddings:
                continue

            # Convert DB list to numpy (Samples, 512)
            db_embs = np.array(movie_embeddings)
            
            # Handle potential nesting issues
            if db_embs.ndim == 1:
                db_embs = db_embs.reshape(1, -1)
            elif db_embs.ndim == 3:
                db_embs = db_embs.reshape(db_embs.shape[0], -1)

            # Calculate similarity for all embeddings of this movie at once
            #sims = cosine_similarity(input_emb, db_embs)
            #current_max = np.mean(sims)
            similarities = cosine_similarity(input_emb, db_embs)
# Take the top 5 matches and average them
            top_5_sims = np.mean(np.sort(similarities[0])[-3:])
            mean_sim = np.mean(top_5_sims)
            if mean_sim > best_overall_sim:
                best_overall_sim = mean_sim
                best_movie_name = movie_name
            #if current_max > best_overall_sim:
              #  best_overall_sim = float(current_max)
              #  best_movie_name = movie_name
            # Add this inside the movie loop
            print(f"Comparing input against DB Movie: {movie_name} | Vector Dim: {db_embs.shape}")

    # 3. Final threshold check
    if best_overall_sim < 0.3:
        return {"movie": "Unknown", "confidence": round(best_overall_sim, 3)}

    # 4. Fetch TMDB details only for the winner
    result = {
        "movie": best_movie_name,
        "confidence": round(best_overall_sim, 3)
    }
    
    tmdb_data = get_tmdb_movie_details(best_movie_name)
    if tmdb_data:
        result.update(tmdb_data)

    return result