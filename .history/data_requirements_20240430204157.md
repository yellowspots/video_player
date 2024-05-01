Data Requirements

    Video Data:
        video_id: Unique identifier for each video.
        title: Title of the video.
        description: A brief description of the video.
        preview_image_url: URL to a preview image of the video.
        theme: Associated weekly theme.
        upload_week: The week the video was uploaded.
        view_count: Number of times the video has been viewed.
        user_rating: Aggregate rating given by users.
        hashtags: List of associated hashtags for categorizing the video.

    Theme Data:
        theme_id: Unique identifier for each theme.
        theme_name: Name of the theme.
        start_date: Date when the theme started.
        end_date: Date when the theme ended.

    User Data (Optional):
        user_id: Unique identifier for each user.
        username: Name of the user.
        profile_picture: URL to the user’s profile picture.

    Miscellaneous Data:
        jokes: Collection of dad jokes to be randomly displayed.


       
"CREATE TABLE videos (\n video_id SERIAL PRIMARY KEY,\n title VARCHAR(255),\n description TEXT,\n preview_image_url TEXT,\n theme VARCHAR(100),\n upload_week DATE,\n view_count BIGINT,\n user_rating DECIMAL(3,2),\n hashtags TEXT[]\n);\n\nCREATE TABLE themes (\n theme_id SERIAL PRIMARY KEY,\n theme_name VARCHAR(100),\n start_date DATE,\n end_date DATE\n);\n\nCREATE TABLE users (\n user_id SERIAL PRIMARY KEY,\n username VARCHAR(100),\n profile_picture TEXT\n);\n\nCREATE TABLE jokes (\n joke_id SERIAL PRIMARY KEY,\n joke_text TEXT\n);"