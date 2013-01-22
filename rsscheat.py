import feedparser

f = open('feeds.dat')

feeds = []

for x in f:
	feeds.append(feedparser.parse(x))

f.close()

for feed in feeds:
	title = feed.feed.title
	try:
		output = open(title +'.dat','w')

		for entry in feed.entries:
			output.write(entry.id + '\n')
	except IOError as e:
		output = open(title+'.dat','w')

		for entry in feed.entries:
			output.write(entry.id + "\n")

