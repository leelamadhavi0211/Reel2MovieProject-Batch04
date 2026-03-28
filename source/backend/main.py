from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload_router
from routers import auth_router
from routers import movie_router
from routers import video_router
from routers import embedding_router

app =APIRouter()

app = FastAPI()

app.include_router(video_router.router)
app.include_router(auth_router.router)
app.include_router(upload_router.router)
app.include_router(movie_router.router)
app.include_router(embedding_router.router)

@app.on_event("startup")
async def print_routes():
    for route in app.routes:
        print(f"Path: {route.path} | Name: {route.name} | Methods: {route.methods}")


@app.get("/")
def home():
    return {"message": "Reel2Movie API Running"}



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)