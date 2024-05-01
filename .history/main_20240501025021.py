from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from typing import List, Optional

app = FastAPI()

DATABASE_URL = os.environ['DATABASE_URL']

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

@app.get("/videos/")
def get_videos(theme_id: Optional[int] = None, search_query: str = '', sort: str = 'upload_date', request: Request):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f"""
    SELECT v.*, c.category_name FROM Videos v
    LEFT JOIN Video_Categories vc ON v.video_id = vc.video_id
    LEFT JOIN Categories c ON vc.category_id = c.category_id
    WHERE (%s IS NULL OR theme_id = %s) AND
    (title ILIKE %s OR description ILIKE %s)
    ORDER BY {sort}
    """
    cur.execute(query, (theme_id, theme_id, f'%{search_query}%', f'%{search_query}%'))
    videos = cur.fetchall()
    cur.close()
    conn.close()
    return videos

@app.get("/videos/{video_id}")
def get_video(video_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Videos WHERE video_id = %s', (video_id,))
    video = cur.fetchone()
    cur.close()
    conn.close()
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@app.post("/videos/", status_code=201)
def create_video(video: dict):
    title = video.get('title')
    description = video.get('description', '')
    preview_image_url = video.get('preview_image_url', '')
    upload_date = video.get('upload_date')
    view_count = video.get('view_count', 0)
    rating_average = video.get('rating_average', 0.0)
    theme_id = video.get('theme_id')

    if not title or theme_id is None:
        raise HTTPException(status_code=400, detail="Title and theme ID are required")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Videos (title, description, preview_image_url, upload_date, view_count, rating_average, theme_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING video_id;
    """, (title, description, preview_image_url, upload_date, view_count, rating_average, theme_id))
    video_id = cur.fetchone()['video_id']
    conn.commit()
    cur.close()
    conn.close()
    return {"video_id": video_id}


@app.get("/categories/")
def get_categories():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Categories')
    categories = cur.fetchall()
    cur.close()
    conn.close()
    return categories

@app.get("/categories/{category_id}/videos")
def get_videos_by_category(category_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT v.* FROM Videos v
        JOIN Video_Categories vc ON v.video_id = vc.video_id
        WHERE vc.category_id = %s
    """, (category_id,))
    videos = cur.fetchall()
    cur.close()
    conn.close()
    return videos

@app.get("/videos/random")
def get_random_video():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Videos ORDER BY RANDOM() LIMIT 1')
    video = cur.fetchone()
    cur.close()
    conn.close()
    if video is None:
        raise HTTPException(status_code=404, detail="No videos found")
    return video
