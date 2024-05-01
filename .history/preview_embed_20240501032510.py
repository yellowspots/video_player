import requests

video_url = 'https://www.tiktok.com/@username/video/1234567890123456789'

oembed_url = f'https://www.tiktok.com/oembed?url={video_url}'

# Making the HTTP request
response = requests.get(oembed_url)
data = response.json()

# Extracting the preview image URL
preview_image_url = data['thumbnail_url']
print(preview_image_url)
