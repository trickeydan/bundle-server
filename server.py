#! /usr/bin/python3

# Bundle Server
# Written in Flask to provide an API

# Written by D.G.Trickey and S.J.McCreery

from flask import Flask, request, render_template
from Song import Song
import json
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
    song_data["idno1"] = Song("idno1").toDict()
    song_data["idno2"] = Song("idno2").toDict()
    song_data["idno3"] = Song("idno3").toDict()
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
