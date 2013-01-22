import feedparser

f = open('feeds.dat')

feeds = []

for x in f:
	feeds.append(feedparser.parse(x))

