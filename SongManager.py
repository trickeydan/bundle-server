import sqlite3
from SpotifyWrapper import SpotifyWrapper

class SongManager(object):

    def __init__(self):
        self.sw = SpotifyWrapper()
        self.playlist_id = ""
        self.offset = 0
        self.curr_song = "53RJvlt7Y2QiJ6b28LaC3t"

        playlists = self.sw.get_playlists()
        number = 1
        playlist_keys = {}
        for key in playlists.keys():
            print(str(number) + ": " + playlists[key])
            playlist_keys[number] = key
            number += 1

        self.playlist_id = playlist_keys[int(input("Please choose a playlist: "))]

    def get_polling_tracks(self):
        return self.sw.get_playlist_tracks(self.playlist_id,offset=5)

    def get_curr_track(self):
        return self.sw.get_track(self.curr_song)

    def curr_expire_time(self):
        return 94320482190
