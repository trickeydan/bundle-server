#! /usr/bin/python3

# Bundle Server
# Written in Flask to provide an API

# (c) 2017 D.G.Trickey and S.J.McCreery

from flask import Flask
app = Flask(__name__)

@app.route('/')
def default():
    return 'Bundle Server'
