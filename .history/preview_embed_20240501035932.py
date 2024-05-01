import requests

share_link = "https://vm.tiktok.com/abc123/"  # Replace with the actual TikTok share link
url = "http://localhost:8000/videos/tiktok"  # Replace with your API endpoint URL

payload = {"share_link": share_link}
response = requests.post(url, json=payload)

if response.status_code == 201:
    print("Video added successfully!")
    print(response.json())
else:
    print("Error adding video:")
    print(response.text)