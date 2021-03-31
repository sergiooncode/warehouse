from mongoengine import Document
from mongoengine import IntField
from mongoengine import StringField


class MongoArticleInventory(Document):
    article_id = StringField(max_length=20)
    name = StringField(max_length=100)
    stock = IntField()
