curl -X POST http://localhost:8000/videos/ -H "Content-Type: application/json" -d '{
    "title": "Sample Video",
    "description": "This is a sample video description.",
    "preview_image_url": "http://example.com/image.jpg",
    "video_url": "https://www.tiktok.com/t/ZPRwfwNxK/",
    "upload_date": "2024-05-01",
    "view_count": 100,
    "rating_average": 4.5,
    "theme_id": 1,
    "category_ids": [1, 2, 3]
}'
