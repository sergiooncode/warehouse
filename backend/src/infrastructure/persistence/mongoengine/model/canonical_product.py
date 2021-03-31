from mongoengine import Document
from mongoengine import EmbeddedDocumentListField
from mongoengine import FloatField
from mongoengine import StringField


class MongoCanonicalProduct(Document):
    name = StringField(max_length=100)
    price = FloatField()
    containing_articles = EmbeddedDocumentListField("MongoCanonicalArticle")
