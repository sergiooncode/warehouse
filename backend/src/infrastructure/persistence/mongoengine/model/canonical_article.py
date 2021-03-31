from mongoengine import EmbeddedDocument
from mongoengine import IntField


class MongoCanonicalArticle(EmbeddedDocument):
    article_id = IntField()
    needed_amount = IntField()
