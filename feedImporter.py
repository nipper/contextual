import feedparser
import peewee
from model import *

def updateFeedEntries(feed):

    parsedFeed = feedparser.parse(feed.url)
    
    for entry in parsedFeed.entries:
        newLink,newTitle = entry.link,entry.title
        try:
            newEntry = Entries.get(Entries.url == entry.link)
        except Entries.DoesNotExist:
            newEntry = Entries(entryTitle='test',url=newLink,feed=feed)
            newEntry.save()


for feed in Feeds.select():
    print(feed.title)

    updateFeedEntries(feed)

