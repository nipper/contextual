from peewee import *

databasePath = 'context.db'

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
	url = CharField()

	
