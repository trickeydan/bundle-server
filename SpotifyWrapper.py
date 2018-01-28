import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

try:
    import spconfig
except:
    print ("You need a config file!")

class SpotifyWrapper(object):

    def __init__(self):
        print("Authenticating with Spotify...")
        #token = util.prompt_for_user_token(spconfig.spot_username,"playlist-read-private,playlist-read-collaborative",client_id=spconfig.spot_client_id,client_secret=spconfig.spot_client_secret,redirect_uri=spconfig.spot_redirect)

        try:

            spo = SpotifyOAuth(spconfig.spot_client_id,spconfig.spot_client_secret,spconfig.spot_redirect,scope="playlist-read-private,playlist-read-collaborative",cache_path=spconfig.spot_cache)
            print("DEBUG")
            print(spo.get_cached_token())
            self.sp = spotipy.Spotify(auth=spo.get_cached_token()["access_token"])
            print(self.sp)
            print("Authenticated.")
        except:
            print("Unable to connect to spotify :(")


    def get_playlists(self):
        playlists = self.sp.user_playlists(spconfig.spot_username)
        if(len(playlists) > 0):
            print("\nAvailable Playlists:")
            arr = {}
            for playlist in playlists['items']:
                arr[playlist['id']] = playlist['name']
            return arr
        else:
            print("No playlists found :(")
            return None

    def get_playlist_tracks(self,playlist_id,offset=0,quantity=5):
        return self.sp.user_playlist_tracks(spconfig.spot_username,playlist_id=playlist_id,fields="items.track.id,items.track.name,items.track.duration_ms,items.track.artists.name,items.track.album.images.url",limit=quantity,offset=offset)

    def get_track(self,track_id):
        return self.sp.track(track_id)
