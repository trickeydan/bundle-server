import spotipy
import spotipy.util as util

try:
    import spconfig
except:
    print ("You need a config file!")

class SpotifyWrapper(object):

    def __init__(self):
        print("Authenticating with Spotify...")
        token = util.prompt_for_user_token(spconfig.spot_username,"playlist-read-private,playlist-read-collaborative",client_id=spconfig.spot_client_id,client_secret=spconfig.spot_client_secret,redirect_uri=spconfig.spot_redirect)

        if token:
            print("Authenticated.")
            self.sp = spotipy.Spotify(auth=token)
        else:
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
