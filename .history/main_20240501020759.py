import os
import asyncpg
from fastapi import FastAPI, Depends
from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="/Users/gene/thought_arc/static", html=True), name="static")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
async def main():
    return {"message": "Hello World"}

class Video(BaseModel):
    title: str
    description: str
    preview_image_url: HttpUrl
    theme: str
    upload_week: str
    view_count: int
    user_rating: float
    hashtags: List[str]

class Theme(BaseModel):
    theme_name: str
    start_date: str
    end_date: str

class User(BaseModel):
    username: str
    profile_picture: HttpUrl

class Joke(BaseModel):
    joke_text: str

async def get_db_connection():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

@app.post("/videos/", response_model=int, status_code=201)
async def create_video(video: Video, db: asyncpg.Connection = Depends(get_db_connection)):
    query = """
    INSERT INTO videos (title, description, preview_image_url, theme, upload_week, view_count, user_rating, hashtags)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8) RETURNING video_id;
    """
    video_id = await db.fetchval(query, video.title, video.description, video.preview_image_url, video.theme,video.upload_week, video.view_count, video.user_rating, video.hashtags)
    return video_id

@app.get("/videos/", response_model=List[Video])
async def list_videos(theme_name: Optional[str] = None, sort: Optional[str] = None, db: asyncpg.Connection = Depends(get_db_connection)):
    base_query = "SELECT * FROM videos"
    where_clause = f" WHERE theme = $1" if theme_name else ""
    order_clause = ""
    if sort == "most_watched":
        order_clause = " ORDER BY view_count DESC"
    elif sort == "most_recent":
        order_clause = " ORDER BY upload_week DESC"
    elif sort == "highest_rated":
        order_clause = " ORDER BY user_rating DESC"
    query = f"{base_query}{where_clause}{order_clause}"
    videos = await db.fetch(query, theme_name) if theme_name else await db.fetch(query)
    return videos

@app.get("/videos/random/", response_model=Video)
async def random_video(db: asyncpg.Connection = Depends(get_db_connection)):
    video = await db.fetchrow("SELECT * FROM videos ORDER BY RANDOM() LIMIT 1")
    return video

@app.get("/jokes/random/", response_model=Joke)
async def random_joke(db: asyncpg.Connection = Depends(get_db_connection)):
    joke = await db.fetchrow("SELECT * FROM jokes ORDER BY RANDOM() LIMIT 1")
    return joke

@app.post("/themes/", response_model=int, status_code=201)
async def create_theme(theme: Theme, db: asyncpg.Connection = Depends(get_db_connection)):
    query = "INSERT INTO themes (theme_name, start_date, end_date) VALUES ($1, $2, $3) RETURNING theme_id;"
    theme_id = await db.fetchval(query, theme.theme_name, theme.start_date, theme.end_date)
    return theme_id

@app.post("/users/", response_model=int, status_code=201)
async def create_user(user: User, db: asyncpg.Connection = Depends(get_db_connection)):
    query = "INSERT INTO users (username, profile_picture) VALUES ($1, $2) RETURNING user_id;"
    user_id = await db.fetchval(query, user.username, user.profile_picture)
    return user_id

@app.post("/jokes/", response_model=int, status_code=201)
async def create_joke(joke: Joke, db: asyncpg.Connection = Depends(get_db_connection)):
    query = "INSERT INTO jokes (joke_text) VALUES ($1) RETURNING joke_id;"
    joke_id = await db.fetchval(query, joke.joke_text)
    return joke_id

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)