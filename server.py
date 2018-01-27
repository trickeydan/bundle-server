#! /usr/bin/python3

# Bundle Server
# Written in Flask to provide an API

# Written by D.G.Trickey and S.J.McCreery

import json
from flask import Flask, request, render_template
import spotipy
import spotipy.util as util
from Song import Song
import spconfig

print("Bundle Server")
print("Authenticating with Spotify...")
token = util.prompt_for_user_token(spconfig.spot_username,"playlist-read-private,playlist-read-collaborative",client_id=spconfig.spot_client_id,client_secret=spconfig.spot_client_secret,redirect_uri=spconfig.spot_redirect)

if token:
    print("Authenticated.")
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(spconfig.spot_username)
    if(len(playlists) > 0):
        print("\nAvailable Playlists:")
        arr = {}
        for playlist in playlists['items']:

            if playlist['owner']['id'] == spconfig.spot_username:
                arr[len(arr) + 1] = playlist['id']
                print(str(len(arr))  + ") " + playlist['name'])
        playlist_id = arr[int(input("Please select a playlist: "))]

    else:
        print("You need to create a playlist.")

else:
    print("Unable to connect to spotify :()")

app = Flask(__name__)

@app.route('/')
def vote():
    return render_template('vote.html')

@app.route('/explore')
def explore():
    return 'User explore page'

@app.route('/api/v1/club/')
def api_info():
    song_data = {}
    song_data["idno1"] = dict(Song("idno1"))
    song_data["idno2"] = dict(Song("idno2"))
    song_data["idno3"] = dict(Song("idno3"))
    club_data = {}
    club_data["name"] = "Timepiece"
    club_data["logo_url"] = "http://www.timepiecenightclub.co.uk/wp-content/uploads/2015/01/TP-logo-WHITE.png"
    club_data["time_expire"] = 1517061942
    club_data["songs"] = song_data
    return json.JSONEncoder().encode(club_data)

@app.route('/api/v1/club/vote', methods=['POST'])
def api_vote():
    if request.method == 'POST':
        return request.form['song_id']
    return "JSSSONNNNN"

@app.errorhandler(404)
def page_not_found(error):
    return "Um, that doesn't exist"

@app.errorhandler(405)
def page_not_found(error):
    return "Incorrect Request Type"
