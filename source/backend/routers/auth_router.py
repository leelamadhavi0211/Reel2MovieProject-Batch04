import datetime

from fastapi import APIRouter, HTTPException, Depends
from auth.dependencies import get_current_user
from database.connection import users_collection
from models.user_model import UserSignup, UserLogin
from auth.hash import hash_password, verify_password
from auth.jwt_handler import create_token
from database.connection import uploads_collection
from database.connection import movies_collection
from pydantic import BaseModel
from typing import List


router = APIRouter()
@router.get("/history")
async def get_history(current_user: dict = Depends(get_current_user)):
    user_email = current_user.get("email")
    
    # 1. Get the list of what the user uploaded
    # DB field is 'user_email', and movie name is in 'movie'
    user_uploads = list(uploads_collection.find({"user_email": user_email}))

    full_history = []
    for upload in user_uploads:
        # 2. Get the title from the 'movie' field
        search_title = upload.get("movie") 

        # 3. Search the 'movies_collection' using the 'name' field
        movie_info = movies_collection.find_one({"name": search_title})

        if movie_info:
            full_history.append({
                "id": str(upload["_id"]),
                "movie_name": search_title, # from uploads
                "poster": movie_info.get("poster"), # from movies_collection
                "overview": movie_info.get("overview"), # from movies_collection
                "date": upload.get("created_at")
            })
            
    return full_history
    
# app.include_router(video_router.router)



@router.post("/signup")
def signup(user: UserSignup):

    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed = hash_password(user.password)

    user_data = {
        "name": user.name,
        "email": user.email,
        "password": hashed
    }

    users_collection.insert_one(user_data)

    return {"message": "User created successfully"}



@router.post("/login")
def login(user: UserLogin):

    db_user = users_collection.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_token({
        "user_id": str(db_user["_id"]),
        "email": db_user["email"]
    })

    return {
        "message": "Login successful",
        "token": token,
        "name": db_user["name"],   # 👈 add this
        "email": db_user["email"]
    }