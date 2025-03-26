from scraper import Scraper
from sp import SP

scraper = Scraper()
sp = SP()
song_names = scraper.get_first_100_titles()

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
song_uris = sp.get_songs(date, song_names=song_names)
playlist = sp.create_playlist(date)
sp.add_items_to_playlist(song_uris)
