from dataclasses import dataclass, field
from datetime import date

from marshmallow.validate import OneOf

from .base import BaseDataclass, SuccessResponse
from .enums import Languages, Currency
from .products import FeaturedProduct


@dataclass
class ProductFullTextSearchResponse(SuccessResponse):
    result: list[FeaturedProduct] = field(
        default_factory=list, metadata={"required": True}
    )


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
