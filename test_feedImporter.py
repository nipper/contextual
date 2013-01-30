import unittest
from model import *
import goblin


class FeedTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        #Connect to the DB
        db.connect()

        #create the appropriate table:

        Feeds.create_table()
        Entries.create_table()

        #Prime the feeds table
        Feeds.get_or_create(url='http://nickpootbenefit.blogspot.com/feeds/posts/default',title='NickPoot')

    def tearDown(self):
        unittest.TestCase.tearDown(self)

        Entries.drop_table()
        Feeds.drop_table()
        db.close()

    def testUpdateFeeds(self):
        

        goblin.updateFeeds()

        self.assertEqual('http://nickpootbenefit.blogspot.com/2009/12/nickpootbenefitorg.html',Entries.get(Entries.id==1).url,'URL Test Works')
        self.assertEqual('NICKPOOTBENEFIT.ORG',Entries.get(Entries.id==1).entryTitle,'Title is working okay')


if __name__ == '__main__':
    unittest.main()

