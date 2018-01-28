import sqlite3
import spconfig
from random import randrange
from SpotifyWrapper import SpotifyWrapper

database = sqlite3.connect(spconfig.db_location)
cursor = database.cursor()

def init_db():
    with open("setup.sql", "r") as script:
        database.executescript(script.read())

def cleanup_db():
    cursor.close()
    database.close()

class SongManager(object):

    def __init__(self):
        self.sw = SpotifyWrapper()
        self.playlist_id = ""
        self.offset = 0
        self.curr_song = "53RJvlt7Y2QiJ6b28LaC3t"

        self.playlist_id = spconfig.spot_playlist


    def get_polling_tracks(self):
        random_offset = randrange(0,50)
        return self.sw.get_playlist_tracks(self.playlist_id,offset=0)

    def get_curr_track(self):
        return self.sw.get_track(self.curr_song)

    def curr_expire_time(self):
        return 94320482190
