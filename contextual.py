# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from model import *
app = Flask(__name__)
app.config.from_object(__name__)

# configuration
DATABASE = 'test_context.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


@app.before_request
def beforeRequest():
    g.db = db
    g.db.connect()
    
@app.teardown_request
def afterRequest(exception):
    g.db.close()

@app.route('/')
def show_feeds():
    feeds = Feeds.select()
    for x in feeds:
        print x.title
    return render_template('index.html',feeds=feeds)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)


