from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

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

class Feeds(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tile = db.Column(db.String(45))
    guid = db.Column(db.String(256), unique=True)
    siteUrl = db.Column(db.String(255))
    feedUrl = db.Column(db.String(255))

    def __init__(self,title,feedUrl):
        self.title = title
        self.feedUrl = feedUrl

    def __repr__(self):
        return '<Feed %r>' % self.title[:15]

class Entry(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    guid = db.Column(db.String(255))
    uri = db.Column(db.String(255))

    feedId =db.Column(db.Integer,db.ForeignKey('Feeds.id'))
    feed = db.relationship('Feeds',backref = db.backref('entry',lazy='dynamic'))

    def __init__(self, title,guid,date,uri,feed):

        self.title,guid,date,uri,feed = title,guid,date,uri,feed




