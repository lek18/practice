import asyncio

import aiohttp
from bs4 import BeautifulSoup
import requests
import os
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://pcg.church/resources/music"
html = requests.get(BASE_URL).text
soup = BeautifulSoup(html, "html.parser")
download_folder = "/Users/luisek/Downloads/music"




albums = {}

for album_div in soup.find_all("div", class_="album collapsed"):
    album_title = album_div.find("div", class_="title").get_text(strip=True)

    playlist_ul = album_div.find("ul", class_="playlist")

    songs = []

    if playlist_ul:
        for li in playlist_ul.find_all("li"):
            span = li.find("span", class_="playable")
            song_name = span.get_text(strip=True) if span else None

            # Use downloadable link if it exists, otherwise fallback to data-url
            link_tag = li.find("a", class_="downloadable")
            download_link = link_tag['href'] if link_tag else (
                span['data-url'] if span and span.has_attr('data-url') else None)

            if song_name and download_link:
                songs.append({
                    "name": song_name,
                    "download": download_link
                })

    albums[album_title] = songs


# Async download function
semaphore = asyncio.Semaphore(4)
async def download_song(session, url, folder, filename):
    folder_path = os.path.join(download_folder, folder)
    os.makedirs(folder_path, exist_ok=True)
    filename = filename.replace("/", " -").replace(":", " -")
    filepath = os.path.join(folder_path, f"{filename}.mp3")
    # Skip if already downloaded
    if os.path.exists(filepath):
        logger.info(f"Skipped: {filepath}")
        return

    async with semaphore:  # Limit concurrency to 3
        try:
            async with session.get(url) as resp:
                resp.raise_for_status()
                with open(filepath, "wb") as f:
                    f.write(await resp.read())
            logger.info(f"Downloaded: {filepath}")
        except Exception as e:
            logger.error(f"Failed {filename}: {e}")


# Main async function
async def download_all(albums):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for album_title, songs in albums.items():
            for song in songs:
                url = song['download']
                # Make absolute URL if needed
                if url.startswith("/"):
                    url = "https://pcg.church" + url
                tasks.append(download_song(session, url, album_title, song['name']))
        await asyncio.gather(*tasks)


# Run
asyncio.run(download_all(albums))