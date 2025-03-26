import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SP:
    def __init__(self):
        self.CLIENT_ID = "test123"
        self.CLIENT_SECRET = "test123"
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="test132",
                client_id=self.CLIENT_ID,
                client_secret=self.CLIENT_SECRET,
                show_dialog=True,
                cache_path="day_46_billboard_hot_100\\token.txt",
                username="test123",
            )
        )
        self.user_id = self.sp.current_user()["id"]
        self.playlist = None

    def get_songs(self, date, song_names):
        song_uris = []
        year = date.split("-")[0]
        for song in song_names:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            print(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        self.song_uris = song_uris
        return song_uris

    def create_playlist(self, date):
        self.playlist = self.sp.user_playlist_create(
            user=self.user_id, name=f"{date} Billboard 100", public=False
        )

    def add_items_to_playlist(self, song_uris):
        self.sp.playlist_add_items(playlist_id=self.playlist["id"], items=song_uris)
