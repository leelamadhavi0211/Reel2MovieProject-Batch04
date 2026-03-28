from pydantic import BaseModel
import yt_dlp
import os
import cv2
import uuid
import shutil
from services.clip_model import predict_movie_from_frames
from database.connection import uploads_collection
import subprocess
from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from auth.dependencies import get_current_user


def extract_frames(video_path):
    os.makedirs("temp", exist_ok=True)

    # clear old frames
    for f in os.listdir("temp"):
        if f.endswith(".jpg"):
            os.remove(os.path.join("temp", f))

    subprocess.run([
        "ffmpeg",
        "-i", video_path,
        "-vf", "fps=1",
        "temp/frame_%03d.jpg",
        "-y"
    ])

    frames = sorted([
        f"temp/{f}" for f in os.listdir("temp") if f.endswith(".jpg")
    ])

    return frames[:10]



router = APIRouter()

class UrlRequest(BaseModel):
    url: str


@router.post("/upload-url")
#async def upload_url(
 #   data: UrlRequest,
 #   user: dict = Depends(get_current_user)  # supports guest if you modified dependency
#):
async def upload_url(data: UrlRequest, user: dict = Depends(get_current_user)):

    # user_email = user.get("email") if user else "guest"
    user_email = user.get("email", "guest")
    # Create a unique ID for this specific request
    
    request_id = str(uuid.uuid4())
    request_dir = os.path.join("temp", request_id)
    os.makedirs(request_dir, exist_ok=True)


    try:
        print("Step 1: API hit")

        url = data.url
        if not url:
            raise HTTPException(status_code=400, detail="URL is required")

        print("Step 2: Downloading video...")

        os.makedirs("temp", exist_ok=True)

        # ✅ yt-dlp options (improved)
        ydl_opts = {
            #'outtmpl': 'temp/video.%(ext)s',
            'outtmpl': f'{request_dir}/video.%(ext)s',
            'format': 'mp4',
            'noplaylist': True,
            'quiet': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        print("Downloaded file:", file_path)

        # ✅ Check file exists
        if not os.path.exists(file_path):
            raise Exception("Downloaded file not found")

        print("Step 3: Extracting frames...")

        cap = cv2.VideoCapture(file_path)

        if not cap.isOpened():
            raise Exception("Failed to open video file")

        frames = []
        count = 0

        while True:
            success, frame = cap.read()
            if not success:
                break

            # 🔥 reduce load (important)
            #if count % 60 == 0:
             #   frame_path = f"temp/frame_{count}.jpg"
              #  cv2.imwrite(frame_path, frame)
              #  frames.append(frame_path)
            if count % 60 == 0:
        # 1. Define new dimensions (Width, Height)
                 #new_width = 224
                # new_height = 224 # Or calculate based on aspect ratio
                 h, w = frame.shape[:2]
    
    # 2. Calculate aspect ratio (Target width = 224)
                 new_width = 224
                 ratio = new_width / float(w)
                 new_height = int(h * ratio)
    
    # 2. Resize the frame
                 resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_AREA)
    
    # 3. Save the small version
                 frame_path = f"{request_dir}/frame_{count}.jpg"
                 cv2.imwrite(frame_path, resized_frame)
                 frames.append(frame_path)

            count += 1

        cap.release()

        print(f"Frames extracted: {len(frames)}")

        # ✅ safety check
        if len(frames) == 0:
            raise Exception("No frames extracted")

        # 🔥 limit frames (performance)
        frames = frames[:5]

        print("Step 4: Running AI model...")

        result = predict_movie_from_frames(frames)

        print("AI Result:", result)

        print("Step 5: Storing in DB...")

        upload_data = {
           # "user_email": user["email"] if user else "guest",
            "user_email": user_email if user_email else "guest",
            "type": "url",
            "movie": result["movie"],
            "confidence": result["confidence"],
            "created_at": datetime.utcnow()
        }

        uploads_collection.insert_one(upload_data)

        print("Step 6: Done")

        # ✅ FINAL RESPONSE
       # ✅ FINAL RESPONSE (Updated to match your AI Result keys)
        return {
        "movie": result.get("movie"),
        "title": result.get("title", "Unknown"), # Maps to TMDB Title
        "overview": result.get("overview", "No description available"),
     "release_date": result.get("release_date", "Unknown"),
        "genres": result.get("genres", []), 
        "confidence": float(result["confidence"]), # Convert np.float64 to standard float
        "poster": result.get("poster"),
        "vote_average": result.get("vote_average", 0),
        "video": {
        "frames": count,
        "resolution": "224x224", # Since we resized
        "duration": f"{count}s"  # Based on 1fps logic
         }
    }

    except Exception as e:
        print("ERROR:", str(e))
        import traceback
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # ✅ THE CLEANUP: This runs even if the code crashes!
        if os.path.exists(request_dir):
            shutil.rmtree(request_dir)
            print(f"Cleaned up directory: {request_dir}")