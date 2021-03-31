from dataclasses import dataclass


@dataclass
class ArticleInventory:
    article_id: str
    name: str
    stock: int
