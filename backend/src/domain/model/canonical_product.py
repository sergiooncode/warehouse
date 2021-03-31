from dataclasses import dataclass
from typing import List

from src.domain.model.canonical_article import CanonicalArticle


@dataclass(frozen=True)
class CanonicalProduct:
    name: str
    price: float
    containing_articles: List[CanonicalArticle]
