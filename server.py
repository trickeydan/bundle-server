#! /usr/bin/python3

# Bundle Server
# Written in Flask to provide an API

# (c) 2017 D.G.Trickey and S.J.McCreery

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def vote():
    return 'User voting page'

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
