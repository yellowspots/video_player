CREATE TABLE videos (
    video_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    preview_image_url TEXT,
    theme VARCHAR(100),
    upload_week DATE,
    view_count BIGINT,
    user_rating DECIMAL(3,2),
    hashtags TEXT[]
);
