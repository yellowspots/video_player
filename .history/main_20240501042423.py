from fastapi import FastAPI, HTTPException, Depends, Request, Query
from fastapi.responses import JSONResponse
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from typing import List, Optional
from dotenv import load_dotenv
import requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

@app.get("/videos/")
def get_videos(request: Request, theme_id: Optional[int] = None, search_query: str = '', sort: str = 'upload_date'):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f"""
    SELECT v.video_id, v.title, v.video_url FROM Videos v
    WHERE (%s IS NULL OR theme_id = %s) AND (title ILIKE %s OR description ILIKE %s)
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

@app.get("/", response_class=HTMLResponse)
def landing_page(request: Request):
    return templates.TemplateResponse("landing_page.html", {"request": request})

@app.post("/videos/", status_code=201)
def create_video(video: dict):
    title = video.get('title', '')
    description = video.get('description', '')
    preview_image_url = video.get('preview_image_url', '')
    video_url = video.get('video_url', '')
    upload_date = video.get('upload_date')
    view_count = video.get('view_count', 0)
    rating_average = video.get('rating_average', 0.0)
    theme_id = video.get('theme_id')
    category_ids = video.get('category_ids', [])

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO Videos (title, description, preview_image_url, video_url, upload_date, view_count, rating_average, theme_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING video_id;
        """, (title, description, preview_image_url, video_url, upload_date, view_count, rating_average, theme_id))
        video_id = cur.fetchone()['video_id']
        conn.commit()

        for category_id in category_ids:
            cur.execute("""
                INSERT INTO Video_Categories (video_id, category_id)
                VALUES (%s, %s);
            """, (video_id, category_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
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

@app.post("/videos/tiktok", status_code=201)
def create_tiktok_video(share_link: str = Query(...)):
    # Resolve the short link to the full TikTok video URL
    response = requests.get(share_link, allow_redirects=False)
    full_url = response.headers['Location']

    # Make a request to the TikTok OEmbed API
    oembed_url = f"https://www.tiktok.com/oembed?url={full_url}"
    response = requests.get(oembed_url)
    data = response.json()

    # Extract the relevant video details
    title = data['title']
    description = data.get('description', '')
    preview_image_url = data['thumbnail_url']
    video_url = full_url
    preview_image_url = data['thumbnail_url']
    # Extract other relevant details as needed

    # Create a new video entry using the extracted details
    video_data = {
        'title': title,
        'description': description,
        'preview_image_url': preview_image_url,
        'video_url': video_url,
        # Set other fields as required
    }

    # Call the existing create_video endpoint to add the video to the database
    return create_video(video_data)
