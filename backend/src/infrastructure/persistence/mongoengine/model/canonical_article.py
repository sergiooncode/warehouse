from mongoengine import EmbeddedDocument
from mongoengine import IntField
from mongoengine import StringField


class MongoCanonicalArticle(EmbeddedDocument):
    article_id = StringField(max_length=20)
    needed_amount = IntField()
