import os
import urllib.parse

import requests
from bs4 import BeautifulSoup


path = "/Users/luisek/Downloads/"
# Function to download the item
def download_item(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        content_length = len(response.content)
        print(f"Content length of {url}: {content_length}")
        if content_length > 0:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
        else:
            print(f"Empty response for {url}")
    else:
        print(f"Failed to download {url}: HTTP status code {response.status_code}")

# Function to extract song name from URL
def extract_song_name(url):
    # Decode URL and replace %20 with space
    decoded_url = urllib.parse.unquote(url)
    # Split the URL by '/' and get the last part (the file name)
    file_name = decoded_url.split('/')[-1]
    # Remove file extension
    song_name = os.path.splitext(file_name)[0]
    return song_name

# URL of the webpage
base_url = 'https://pcg.church/resources/music'

# Send a GET request to the webpage
response = requests.get(base_url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all clickable items on the webpage with class 'downloadable'
items = soup.find_all('a', class_='downloadable')


# Iterate through each item and download it
for i, item in enumerate(items[0:10]):
    if '.mp3' in item['href']:  # Check if the link contains '.mp3'
        item_url = item['href']  # Get the MP3 download link
        if not item_url.startswith('http'):  # Check if the link is absolute
            item_url = "https://pcg.church" + item_url  # Convert relative URL to absolute URL
        # Extract song name from URL
        song_name = extract_song_name(item_url).replace("_", "")
        filename = f'{path}{song_name}.mp3'
        print(f'Downloading item {i+1}...')
        download_item(item_url, filename)


# a="https://pcg.church/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MiwicHVyIjoiYmxvYl9pZCJ9fQ==--964d3a5dcffca41651d50d517d29b061f1bbf470/P.%201_%20Blest%20and%20Happy%20Is%20the%20Man.mp3?disposition=attachment"