import feedparser
import peewee
from model import *

feeds = peewee.SelectQuery(Feeds,Feeds.id,Feeds.url,Feeds.title)

for feed in feeds:
	
	ufeed = feedparser.parse(feed.url)

	for entry in ufeed.entries:
		print entry.title
		try:
			newEntry = Entries.get(Entries.url == entry.link)
			print("Entries.already in DB")
		except Entries.DoesNotExist:
			Entries.create(url = entry.link,feed=Feeds.get(Feeds.url == ufeed.link))
			print('Entries.created')

		
