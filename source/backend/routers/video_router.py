from fastapi import APIRouter, UploadFile, File
import uuid
import os

from services.video_service import extract_frames
from services.embedding_service import get_frame_embedding
from services.matching_service import match_video
from services.audio_service import extract_audio, recognize_audio
from services.fusion_service import fuse_results
from services.tmdb_services import get_tmdb_movie_details

router = APIRouter()

results_store = {}


@router.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):

    video_id = str(uuid.uuid4())
    path = f"temp/{video_id}.mp4"

    with open(path, "wb") as f:
        f.write(await file.read())

    # 1. Frames
    frames = extract_frames(path)

    # 2. Embeddings
    embeddings = [get_frame_embedding(f) for f in frames]

    # 3. Match
    video_result = match_video(embeddings)

    # 4. Audio
    audio_path = extract_audio(path)
    audio_result = recognize_audio(audio_path)

    # 5. Fusion
    movie, confidence = fuse_results(video_result, audio_result)

    # 6. TMDB
    details = get_tmdb_movie_details(movie)

    result = {
        "movie": movie,
        "confidence": round(confidence * 100, 2),
        "audio_match": audio_result["audio_match"],
        "video_match": video_result[0],
        "poster": details.get("poster"),
        "genre": details.get("genre")
    }

    results_store[video_id] = result

    return {"id": video_id}