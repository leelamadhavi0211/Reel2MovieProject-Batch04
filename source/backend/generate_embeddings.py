from datetime import datetime
import os
import cv2
import requests
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from database.connection import embeddings_collection

device = "cuda" if torch.cuda.is_available() else "cpu"

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_embedding(frame):
    # Convert BGR to RGB
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.get_image_features(**inputs)

    # FIX: Handle potential 'BaseModelOutputWithPooling' object
    if not torch.is_tensor(outputs):
        # Some CLIP versions return an object; extract the pooler_output tensor
        emb = outputs.pooler_output if hasattr(outputs, 'pooler_output') else outputs[0]
    else:
        emb = outputs

    # Normalize the tensor
    emb = emb / emb.norm(dim=-1, keepdim=True)
    
    # Return as a flat numpy array
    return emb.cpu().numpy().flatten()


def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30

    embeddings = []
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % int(fps) == 0:
            if frame.mean() < 30:
                count += 1
                continue

            emb = get_embedding(frame)
            embeddings.append(emb.tolist())

        count += 1

    cap.release()
    return embeddings[:40]


#DATASET = "dataset"

"""
# --- DEBUG ADDITIONS ---
print(f"Checking dataset folder: {os.path.abspath(DATASET)}")
movie_folders = [f for f in os.listdir(DATASET) if os.path.isdir(os.path.join(DATASET, f))]
print(f"Found {len(movie_folders)} movie folders: {movie_folders}")
# --- CORRECT LOOP STRUCTURE ---
for movie in os.listdir(DATASET):
    folder = os.path.join(DATASET, movie)
    if not os.path.isdir(folder): continue

    # CRITICAL: This must be INSIDE the movie loop to reset for each movie
    movie_specific_embeddings = [] 

    for file in os.listdir(folder):
        if file.endswith(".mp4"):
            path = os.path.join(folder, file)
            # Extract frames for THIS specific video
            new_frames = process_video(path)
            movie_specific_embeddings.extend(new_frames)

    if movie_specific_embeddings:
        print(f"Saving {len(movie_specific_embeddings)} unique embeddings for {movie}")
        embeddings_collection.update_one(
            {"movie_name": movie},
            {"$set": {
                "movie_name": movie,
                "embeddings": movie_specific_embeddings, # Now unique to this movie
                "updated_at": datetime.now()
            }},
            upsert=True
        )
     #print(f"DB Update Result: Matched={result.matched_count}, Upserted={result.upserted_id}")
     """
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(BASE_DIR, "dataset")

print(f"Checking dataset folder: {DATASET}")

if not os.path.exists(DATASET):
    print(f"[ERROR] Dataset folder not found at: {DATASET}")
else:
    movie_folders = [f for f in os.listdir(DATASET) if os.path.isdir(os.path.join(DATASET, f))]
    print(f"Found {len(movie_folders)} movie folders: {movie_folders}")

    for movie in movie_folders:
        folder = os.path.join(DATASET, movie)
        movie_specific_embeddings = [] 

        print(f"\n>>> Processing Movie: {movie}")
        
        for file in os.listdir(folder):
            if file.lower().endswith(".mp4"):
                path = os.path.join(folder, file)
                print(f"    - Extracting from: {file}")
                new_frames = process_video(path)
                movie_specific_embeddings.extend(new_frames)

        # SAVE TO DATABASE
        if movie_specific_embeddings:
            payload = {
                "movie_name": movie,
                "embeddings": movie_specific_embeddings
                #"embeddings": all_embeddings_as_list
            }
            # Send to your new FastAPI endpoint
            try:
                response = requests.post("http://127.0.0.1:8000/upload-embeddings", json=payload)
                
                if response.status_code == 200:
                    print(f"✓ Successfully uploaded {movie} to API")
                    print(f"  Response: {response.json()}")
                else:
                    print(f"✗ Failed to upload {movie}: {response.status_code}")
                    print(f"  Response: {response.text}")
            except Exception as e:
                print(f"✗ Error uploading {movie}: {str(e)}")
        else:
            print(f"  No embeddings found for {movie}")

print("\n--- All tasks complete ---")