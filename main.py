import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


#Scraping Billboard
year = input('Which year would you like to travel to? Type it in YYYY format: ')
month = input('Which month would you like to travel to? Type it in MM format: ')
day = input('Which day would you like to travel to? Type it in DD format: ')
date = f"{year}-{month}-{day}"
url = f'https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/'
response = requests.get(url)
billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")
all_song = soup.select("li ul li h3")
print()
song_name = [song.getText(strip=True) for song in all_song]

print(song_name)
CLIENT_ID = "447643cef8ea4bf38686fbebfd481a06"
CLIENT_SECRET = "9831d46cd37e4486a00082e2451b557c"
SPOTIPY_REDORECT ="http://localhost:8888/callback"

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDORECT,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#search Spotify for songs by title
song_uris  = []
year1 = date.split("-")[0]
for song in song_name:
    result = sp.search(q=f"track: {song} year: {year1}", type="track")
    print(result)
    try:
        uri= result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesnt exis in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
