
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

def load_environment():
    """Loads environment variables from the .env file."""
    load_dotenv()

def get_billboard_top_100(date: str) -> list:
    """Scrapes the Billboard Hot 100 songs for a specific date."""
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    songs = soup.select("li ul li h3")
    return [song.getText().strip() for song in songs]

def authenticate_spotify() -> spotipy.Spotify:
    """Authenticates with Spotify and returns a Spotipy client."""
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=os.getenv("REDIRECT_URI"),
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            show_dialog=True,
            cache_path="token.txt"
        )
    )

def search_spotify_uris(sp: spotipy.Spotify, song_names: list, year: str) -> list:
    """Searches for song URIs on Spotify given a list of song names and a year."""
    uris = []
    for song in song_names:
        try:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            uri = result["tracks"]["items"][0]["uri"]
            uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
        except Exception as e:
            print(f"An error occurred while searching for {song}: {e}")
    return uris

def create_spotify_playlist(sp: spotipy.Spotify, user_id: str, date: str, uris: list):
    """Creates a new private Spotify playlist and adds the found songs."""
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=uris)
    print(f"Playlist '{playlist['name']}' created successfully!")

def main():
    load_environment()
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    songs = get_billboard_top_100(date)
    sp = authenticate_spotify()
    user_id = sp.current_user()["id"]
    uris = search_spotify_uris(sp, songs, date.split("-")[0])
    create_spotify_playlist(sp, user_id, date, uris)

if __name__ == "__main__":
    main()
