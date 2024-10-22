from dataclasses import dataclass, field
from datetime import date

from marshmallow.validate import Length, OneOf, Range

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import Currency


@dataclass
class Category(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    name_ru: str = field(metadata={"validate": Length(max=150, min=1)})
    parent_id: int | None = field(
        metadata={
            "strict": True,
        }
    )
    slug: str = field(metadata={"validate": Length(max=100, min=1)})
    is_visible: bool = field(default=True)
    weight: int = field(default=0)


@dataclass
class CreateCategoryRequest(BaseDataclass):
    name: str = field(metadata={"validate": Length(max=150, min=1)})
    slug: str = field(metadata={"validate": Length(max=100, min=1)})
    return_percent: int = field(metadata={"validate": Range(min=0, max=100)})
    parent_id: int | None = field(
        metadata={
            "strict": True,
        },
        default=None,
    )
    is_visible: bool | None = field(default=None)
    weight: int = field(default=0)
    tags: list[int] | None = field(default_factory=list)


@dataclass
class CategoryResponse(SuccessResponse):
    result: Category = field()


@dataclass
class CategoriesResponse(PagedResponse):
    result: list[Category] = field(default_factory=list, metadata={"required": True})


@dataclass
class TagCounter(BaseDataclass):
    tag_id: int = field(metadata={"strict": True})
    count: int = field(metadata={"strict": True})


@dataclass
class FilterCounterResult(BaseDataclass):
    count: int = field(metadata={"strict": True})
    tags: list[TagCounter] = field(default_factory=list, metadata={"required": True})


@dataclass
class FilterCounterResponse(SuccessResponse):
    result: FilterCounterResult = field()


@dataclass
class FilterCounterRequest(BaseDataclass):
    delivery_date: date = field()
    city_id: int = field(metadata={"strict": True})
    category_id: int = field(metadata={"strict": True})
    price_from: int | None = field(metadata={"strict": True})
    price_to: int | None = field(metadata={"strict": True})
    promo_code: str = field()
    currency: str = field(
        metadata={"validate": OneOf([r.value for r in Currency])}, default="rub"
    )
    selected: list[int] = field(default_factory=list, metadata={"required": True})
    ids: list[int] = field(default_factory=list, metadata={"required": True})
