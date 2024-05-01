from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
import os
import asyncpg
from fastapi.concurrency import run_in_threadpool

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

class Video(BaseModel):
    title: str = Field(..., max_length=255)
    description: str
    preview_image_url: HttpUrl
    theme: str = Field(..., max_length=100)
    upload_week: str
    view_count: int
    user_rating: float
    hashtags: List[str]

class Theme(BaseModel):
    theme_name: str = Field(..., max_length=100)
    start_date: str
    end_date: str

class User(BaseModel):
    username: str = Field(..., max_length=100)
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
    video_id = await db.fetchval(query, video.title, video.description, video.preview_image_url, video.theme,
                                 video.upload_week, video.view_count, video.user_rating, video.hashtags)
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

# Additional async endpoints as needed...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
