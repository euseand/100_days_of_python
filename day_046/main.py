import bs4 as bs
import requests as r
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_ID = "9acb805d225840b6bef00293f33369fe"
SPOTIFY_SECRET = "3f3e0e0fbd07446fb74c7fb9a27336f1"
SPOTIFY_URL = "http://example.com"

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri=SPOTIFY_URL,
        scope="playlist-modify-private",
        show_dialog=True,
    )
)

print(spotify.current_user())
user_id = spotify.current_user().get("id")

date = input("What date you want to check the Billboard Hot 100 songs list? (format is yyyy-mm-dd): ")

page = r.get(f"https://www.billboard.com/charts/hot-100/{date}").text
soup = bs.BeautifulSoup(page, "html.parser")

songs = soup.findAll("span", class_="chart-element__information__song text--truncate color--primary")
songs = [song.getText() for song in songs]

artists = soup.findAll("span", class_="chart-element__information__artist text--truncate color--secondary")
artists = [artist.getText() for artist in artists]

songs = list(zip(songs, artists))

searches = []

song_uris = []
for song in songs:
    search = spotify.search(q=f"track:{song[0]}", type="track")
    try:
        song_uris.append(search.get("tracks").get("items")[0].get("uri"))
    except IndexError:
        print(f"Song {song[0]} by {song[1]} does not exist in Spotify. Skipped. ")

playlist = spotify.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

spotify.playlist_add_items(playlist_id=playlist.get("id"), items=song_uris)

