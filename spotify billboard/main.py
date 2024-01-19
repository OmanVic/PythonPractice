import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth
# music_date = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD:")
#
#
#
#
# url = f"https://www.billboard.com/charts/hot-100/{music_date}"
# response = requests.get(url)
# data = response.text
# soup = BeautifulSoup(data, "html.parser")
# title = [title.getText().strip() for title in soup.select("li ul li h3")]
# print(title)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="decab8a03813442d91f7bc12906c2162",
        client_secret="d2b29f20e5864afbaa65a80859160e2f",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]