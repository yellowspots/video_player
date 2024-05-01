import requests

with open('your_csv_file.csv', 'r') as file:
    all_lines = file.readlines()
# Parse each line manually, skipping the header
data_lines = all_lines[1:]  # Skip header

# Prepare to store the results
results = []

for line in data_lines:
    # Split the line into components assuming a comma as the main delimiter
    components = line.strip().split('","')
    # Clean up quotes and newlines
    link = components[0].replace('"', '')
    description = components[1]
    tags = components[2].replace('"', '')

    # Construct the OEmbed URL
    oembed_url = f'https://www.tiktok.com/oembed?url={link}'

    # Make the HTTP request
    response = requests.get(oembed_url)
    if response.status_code == 200:
        data = response.json()
        preview_image_url = data.get('thumbnail_url', 'No thumbnail URL found')
    else:
        preview_image_url = 'Failed to retrieve'

    # Append the result
    results.append({
        'Link': link,
        'Description': description,
        'Tags': tags,
        'Thumbnail URL': preview_image_url
    })

# Display the results
for result in results:
    print(result)
