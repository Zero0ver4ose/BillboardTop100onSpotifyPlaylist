import requests
from bs4 import BeautifulSoup

year = input('Which year would you like to travel to? Type it in YYYY format: ')
month = input('Which month would you like to travel to? Type it in MM format: ')
day = input('Which day would you like to travel to? Type it in DD format: ')

url = f'https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/'

response = requests.get(url)
billboard = response.text

soup = BeautifulSoup(billboard, "html.parser")

all_song = soup.select("li ul li h3")

print()

song_name = [song.getText(strip=True) for song in all_song]

print(song_name)
