import requests

share_link = "https://www.tiktok.com/t/ZPRwfwNxK/"  # Replace with the actual TikTok share link
url = "http://localhost:8000/videos/tiktok"  # Replace with your API endpoint URL

params = {"share_link": share_link}
response = requests.post(url, paramas=params)

if response.status_code == 201:
    print("Video added successfully!")
    print(response.json())
else:
    print("Error adding video:")
    print(response.text)