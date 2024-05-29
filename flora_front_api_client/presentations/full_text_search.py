from dataclasses import dataclass, field
from datetime import date

from .base import BaseDataclass, PagedResponse


@dataclass
class Product(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    city: str = field()
    country: str = field()
    name: str = field()
    description: str = field()
    tags: str = field()
    category: str = field()
    compound: str = field()
    image: str = field()
    revision: int = field(metadata={"strict": True})


@dataclass
class ProductFullTextSearchResponse(PagedResponse):
    result: list[Product] = field(default_factory=list, metadata={"required": True})


@dataclass
class ProductFullTextSearchRequest(BaseDataclass):
    term: str = field()
    city_id: int = field(metadata={"strict": True})
    delivery_date: date = field()
