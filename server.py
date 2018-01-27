#! /usr/bin/python3

# Bundle Server
# Written in Flask to provide an API

# Written by D.G.Trickey and S.J.McCreery

import json
from flask import Flask, request, render_template
from Song import Song
from SpotifyWrapper import SpotifyWrapper

print("Bundle Server")

sw = SpotifyWrapper()

playlists = sw.get_playlists()
number = 1
playlist_keys = {}
for key in playlists.keys():
    print(str(number) + ": " + playlists[key])
    playlist_keys[number] = key
    number += 1

playlist = playlist_keys[int(input("Please choose a playlist: "))]

app = Flask(__name__)

@app.route('/')
def vote():
    return render_template('vote.html')

@app.route('/explore')
def explore():
    return 'User explore page'

@app.route('/api/v1/club/')
def api_info():
    song_data = sw.get_playlist_tracks(playlist)
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
    return "Um, that doesn't exist", 404

@app.errorhandler(405)
def page_not_found(error):
    return "Incorrect Request Type", 405
