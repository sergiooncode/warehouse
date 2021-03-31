from mongoengine import Document
from mongoengine import EmbeddedDocumentListField
from mongoengine import FloatField
from mongoengine import StringField

from src.infrastructure.persistence.mongoengine.model.canonical_article import MongoCanonicalArticle  # noqa


class MongoCanonicalProduct(Document):
    name = StringField(max_length=100)
    price = FloatField()
    containing_articles = EmbeddedDocumentListField("MongoCanonicalArticle")
