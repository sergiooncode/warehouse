from dataclasses import dataclass


@dataclass(frozen=True)
class CanonicalArticle:
    article_id: int
    needed_amount: int
