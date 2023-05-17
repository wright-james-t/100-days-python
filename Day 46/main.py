from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sys
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.parse
import re

# Load info from .env
load_dotenv()

# Set necessary vars from .env
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

# Specifying format for date validation
date_format = '%Y-%m-%d'

# Get date from user
user_date = input("Provide a date (YYYY-MM-DD): ")
today_date = datetime.now().date()


# Validating user input
try:
    user_date_formatted = datetime.strptime(user_date, date_format).date()
except ValueError:
    print("Incorrect format, please use YYYY-MM-DD. e.g. Input: 1991-08-19 - This would be August 19th, 1991.")
    sys.exit()

if today_date < user_date_formatted:
    print(f"Please choose a date in the past.\nChosen date: {user_date}\nTodays date: {today_date}")
    sys.exit()

# Splitting the date for validation
user_date_list = [int(num) for num in user_date.split('-')]
user_year = user_date_list[0]
user_month = user_date_list[1]
user_day = user_date_list[2]

# Specifying the URL to perform the look up at
user_url = f"https://www.billboard.com/charts/hot-100/{user_date_formatted}"

# Not allowing dates that are older than the oldest allowed date
if user_year < 1958 or user_year == 1958 and user_day < 8 \
        or user_year == 1958 and user_month >= 8 and user_day < 4:
    print("The oldest available date is August 4th, 1958. Please choose a date on or after that specification.")
    sys.exit()

# Pulling the HTML data for the specified date
billboard_url_lookup = requests.get(user_url).text

# Making the soup
soup = BeautifulSoup(billboard_url_lookup, "html.parser")

# Pull all the elements for the song ids, strip spaces, then make a list
song_list_html = soup.select(selector="li ul li h3")
artist_list_html = soup.find_all(name="span", class_='u-letter-spacing-0021')
song_names = [song.text.strip() for song in song_list_html]
artist_names = [artist.text.strip() for artist in artist_list_html]

# Authenticate with spotify
scope = "playlist-modify-private, playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# A gigantic mess of try except statements because the scraped data isn't reliable, need to find a better way to do this
song_uri_list = []
for index in range(len(song_names)):
    song = song_names[index]
    artist = artist_names[index]
    try:
        search_results = sp.search(q=urllib.parse.quote(f"track:{song} artist:{artist}"), limit=10, offset=0,
                                   type="track", market=None)
        song_uri = search_results["tracks"]["items"][0]["uri"]
        artist_name = search_results["tracks"]["items"][0]["artists"][0]["name"]
        song_name = search_results["tracks"]["items"][0]["name"]
        print(f"{artist_name} - {song_name} - {song_uri}")
        song_uri_list.append(song_uri)
    except IndexError:
        print(f"\n\nSong not found using method 1:\nArtist: {artist}\nSong: {song}\n\nRaw Search Results:\n{search_results}\n\nTrying method 2")
        search_results = sp.search(q=f"track:{song} artist:{artist}", limit=10, offset=0, type="track", market=None)
        try:
            song_uri = search_results["tracks"]["items"][0]["uri"]
            artist_name = search_results["tracks"]["items"][0]["artists"][0]["name"]
            song_name = search_results["tracks"]["items"][0]["name"]
            print(f"{artist_name} - {song_name} - {song_uri}")
            song_uri_list.append(song_uri)
        except IndexError:
            print(f"\n\nSong not found using method 2:\nArtist: {artist}\nSong: {song}\n\nRaw Search Results:\n{search_results}\n\nTrying method 3")
            artist = artist.replace("&", "")
            search_results = sp.search(q=f"track:{song} artist:{artist}", limit=10, offset=0, type="track", market=None)
            try:
                song_uri = search_results["tracks"]["items"][0]["uri"]
                artist_name = search_results["tracks"]["items"][0]["artists"][0]["name"]
                song_name = search_results["tracks"]["items"][0]["name"]
                print(f"{artist_name} - {song_name} - {song_uri}")
                song_uri_list.append(song_uri)
            except IndexError:
                print(
                    f"\n\nSong not found using method 3:\nArtist: {artist}\nSong: {song}\n\nRaw Search Results:\n{search_results}\n\nTrying method 4.")
                artist = artist.replace("&", "").replace("Featuring", "").replace("Feature", "").replace("Feat", "")
                search_results = sp.search(q=f"track:{song} artist:{artist}", limit=10, offset=0, type="track",market=None)
                try:
                    song_uri = search_results["tracks"]["items"][0]["uri"]
                    artist_name = search_results["tracks"]["items"][0]["artists"][0]["name"]
                    song_name = search_results["tracks"]["items"][0]["name"]
                    print(f"{artist_name} - {song_name} - {song_uri}")
                    song_uri_list.append(song_uri)
                except IndexError:
                    print(
                        f"\n\nSong not found using method 4:\nArtist: {artist}\nSong: {song}\n\nRaw Search Results:\n{search_results}\n\nTrying method 5.")
                    artist = artist.replace("&", "").replace("Featuring", "").replace("Feature", "").replace("Feat", "")
                    song = re.sub(r"\(.*\)", "", song)
                    song = song.replace("'", "")
                    search_results = sp.search(q=f"track:{song} artist:{artist}", limit=10, offset=0, type="track",
                                               market=None)
                    try:
                        song_uri = search_results["tracks"]["items"][0]["uri"]
                        artist_name = search_results["tracks"]["items"][0]["artists"][0]["name"]
                        song_name = search_results["tracks"]["items"][0]["name"]
                        print(f"{artist_name} - {song_name} - {song_uri}")
                        song_uri_list.append(song_uri)
                    except IndexError:
                        print(
                            f"\n\nSong not found using method 5:\nArtist: {artist}\nSong: {song}\n\nRaw Search Results:\n{search_results}\n\nExiting.")
                        sys.exit()


spotify_user_id = sp.current_user()["id"]
playlist_name = f"{user_date} Billboard Top 100"


def build_playlist():
    sp.user_playlist_create(spotify_user_id, f"{playlist_name}", public=False, collaborative=False,
                            description=f"Playlist of the top 100 songs for {user_date}")
    playlists = sp.user_playlists(spotify_user_id)
    for index_playlist_id in range(len(playlists["items"])):
        if playlists["items"][index_playlist_id]["name"] == playlist_name:
            playlist_id = playlists["items"][index_playlist_id]["id"]
            sp.playlist_add_items(playlist_id, items=song_uri_list, position=None)


build_playlist()
