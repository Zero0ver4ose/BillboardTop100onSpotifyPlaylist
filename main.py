import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


'''year = input('Which year would you like to travel to? Type it in YYYY format: ')
month = input('Which month would you like to travel to? Type it in MM format: ')
day = input('Which day would you like to travel to? Type it in DD format: ')'''
CLIENT_ID = "447643cef8ea4bf38686fbebfd481a06"
CLIENT_SECRET = "9831d46cd37e4486a00082e2451b557c"
SPOTIPY_REDORECT ="http://localhost:8888/callback"

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

'''url = f'https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/'

response = requests.get(url)
billboard = response.text

soup = BeautifulSoup(billboard, "html.parser")

all_song = soup.select("li ul li h3")

print()

song_name = [song.getText(strip=True) for song in all_song]

print(song_name)'''
