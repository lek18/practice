import logging
import os
import urllib.parse
import aiohttp
import asyncio
from bs4 import BeautifulSoup

path = "/Users/luisek/Downloads/"

# Function to download the item asynchronously
async def download_item(session, url_filename, semaphore):
    url, filename = url_filename
    async with semaphore:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.read()
                    with open(filename, 'wb') as f:
                        f.write(data)
                else:
                    logging.error(f"Failed to download {url}: HTTP status code {response.status}")
        except Exception as e:
            logging.error(f"Failed to download {url}: {e}")

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
async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

html = asyncio.run(fetch_html(base_url))

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all clickable items on the webpage with class 'downloadable'
items = soup.find_all('a', class_='downloadable')

# Create a directory to save the downloaded items
if not os.path.exists(path):
    os.makedirs(path)

# Create a list of tuples containing (url, filename)
urls_filenames = []
for i, item in enumerate(items):
    if '.mp3' in item['href']:  # Check if the link contains '.mp3'
        item_url = item['href']  # Get the MP3 download link
        if not item_url.startswith('http'):  # Check if the link is absolute
            item_url = "https://pcg.church" + item_url  # Convert relative URL to absolute URL
        # Extract song name from URL
        song_name = extract_song_name(item_url).replace("_", "")
        filename = f'{path}{song_name}.mp3'
        urls_filenames.append((item_url, filename))

# Limit the number of concurrent requests to 5 using a semaphore
semaphore = asyncio.Semaphore(5)

# Download items asynchronously
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download_item(session, url_filename, semaphore) for url_filename in urls_filenames]
        await asyncio.gather(*tasks)

asyncio.run(main())
print('Download complete!')
