from dataclasses import dataclass, field
from datetime import date

from marshmallow.validate import OneOf, Range

from .base import BaseDataclass, SuccessResponse, Pager
from .enums import Languages, Currency
from .products import FeaturedProduct


@dataclass
class ProductFullTextSearchResponse(SuccessResponse):
    result: list[FeaturedProduct] = field(
        default_factory=list, metadata={"required": True}
    )
    pager: Pager | None = field(default=None)


@dataclass
class ProductFullTextSearchRequest(BaseDataclass):
    term: str = field()
    city_id: int = field(metadata={"strict": True})
    lang: str = field(metadata={"validate": OneOf([p.value for p in Languages])})
    delivery_date: date = field()
    promo: str | None = field(default=None)
    currency: str = field(
        metadata={"validate": OneOf([r.value for r in Currency])}, default="rub"
    )
    page: int = field(default=1, metadata={"validate": Range(min=1)})
    per_page: int = field(default=30, metadata={"validate": Range(min=1, max=60)})
    sort: str = field(
        default="relevance",
        metadata={"validate": OneOf(["relevance", "price", "-price"])},
    )


@dataclass
class SiteSearchHit(BaseDataclass):
    """Категория каталога или текстовая страница. URL строит фронт:
    категория — /{город}/{slug}/, страница — /pages/{slug}."""

    kind: str = field(metadata={"validate": OneOf(["category", "page"])})
    slug: str = field()
    title: str = field()
    snippet: str = field(default="")


@dataclass
class SiteFullTextSearchResponse(SuccessResponse):
    result: list[SiteSearchHit] = field(
        default_factory=list, metadata={"required": True}
    )
    # варианты запроса для подсказок: «розы красные», «розы кустовые»
    suggestions: list[str] = field(default_factory=list)


@dataclass
class SiteFullTextSearchRequest(BaseDataclass):
    term: str = field()
    lang: str = field(metadata={"validate": OneOf([p.value for p in Languages])})
    limit: int = field(default=10, metadata={"validate": Range(min=1, max=50)})
    # для подсказок: страницы только по названию, без совпадений в тексте
    title_only: bool = field(default=False)
