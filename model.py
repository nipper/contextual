from peewee import *

databasePath = 'test.db'

db = SqliteDatabase(databasePath)
class BaseModel(Model):
	class Meta:
		database = db

class Feeds(BaseModel):
	id = IntegerField(primary_key = True)
	url = CharField()
	title = CharField()

	class MetaL:
		database = db


class Entries(BaseModel):
	id = IntegerField(primary_key = True)
	feed = ForeignKeyField(Feeds,related_name='entries')
	entryTitle = CharField()
	url = CharField()


class Users(BaseModel):
    id = IntegerField(primary_key = True)
    firstName = CharField()
    lastName = CharField()
    usernme = CharField()

    def fullName(self):
        return self.firstName + " " + self.lastName

class ReadEntries(BaseModel):

    id = IntegerField(primary_key = True)

    user = ForeignKeyField(Users,related_name='entriesRead')
    entry = ForeignKeyField(Entries,related_name="readBy")
