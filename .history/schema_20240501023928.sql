-- Creating the Videos Table
CREATE TABLE Videos (
    video_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    preview_image_url VARCHAR(255),
    upload_date DATE,
    view_count INT,
    rating_average FLOAT,
    theme_id INT
);

-- Creating the Categories Table
CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255),
    description TEXT
);

-- Creating the Video_Categories Table
CREATE TABLE Video_Categories (
    video_category_id SERIAL PRIMARY KEY,
    video_id INT REFERENCES Videos(video_id),
    category_id INT REFERENCES Categories(category_id)
);