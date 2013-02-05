from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  firstName = db.Column(db.String(25))
  lastName = db.Column(db.String(25))
  password = db.Column(db.String(25))


  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __repr__(self):
    return '<User %r>' % self.username

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    guid = db.Column(db.String(255))
    uri = db.Column(db.String(255))


    feed_id = db.Column(db.Integer, db.ForeignKey('feed.id'))
    feed = db.relationship('Feed',
        backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, title, guid, uri,feed):
        self.title = title
        self.guid = guid
        self.uri = uri
        self.feed = feed

    def __repr__(self):
        return '<Entry %r>' % self.title


class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    title = db.Column(db.String(45))
    siteUrl = db.Column(db.String(255))
    feedUrl = db.Column(db.String(255))

    def __init__(self, name,siteUrl,feedUrl):
        self.name = name
        self.siteUrl = siteUrl
        self.feedUrl = feedUrl

    def __repr__(self):
        return '<feed %r>' % self.name


