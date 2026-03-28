import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["reel2movie"]

users_collection = db["users"]

uploads_collection = db["uploads"]

movies_collection = db["movies"]

results_collection = db["results"]

embeddings_collection = db["embeddings"]