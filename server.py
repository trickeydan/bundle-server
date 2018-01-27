#! /usr/bin/python3

# Bundle Server
# Written in Flask to provide an API

# Written by D.G.Trickey and S.J.McCreery

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def vote():
    return render_template('vote.html')

@app.route('/explore')
def explore():
    return 'User explore page'

@app.route('/api/v1/club/')
def api_info():
    return 'JSONNNNN'

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
