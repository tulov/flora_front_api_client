from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from marshmallow.validate import Length, OneOf

from .base import BaseDataclass, SuccessResponse, PagedResponse, Querystring
from .categories import Category
from .enums import Currency, UnitOfWeight, UnitOfSize, UnitOfCount, ProductTypes
from .images import Image


@dataclass
class Price:
    general: Decimal
    personal: Decimal


@dataclass
class RangePrice:
    start: int
    end: int
    general: Decimal
    personal: Decimal


@dataclass
class PriceWithCurrency:
    usd: Price
    rub: Price
    eur: Price
    kzt: Price


@dataclass
class RangePrices:
    usd: list[RangePrice]
    rub: list[RangePrice]
    eur: list[RangePrice]
    kzt: list[RangePrice]


@dataclass
class Prices:
    mono: RangePrices | None
    bouquet: PriceWithCurrency | None
    gift: PriceWithCurrency | None


@dataclass
class DeliveryPrices:
    usd: Price
    rub: Price
    eur: Price
    kzt: Price


@dataclass
class ProductBaseDataclass(BaseDataclass):
    name: str = field(metadata={"validate": Length(max=150, min=1)})
    description: str | None | None = field(metadata={"validate": Length(max=1000)})
    data: Any | None = field()
    revision: int = field(
        metadata={
            "strict": True,
        }
    )
    size_unit: str = field(metadata={"validate": OneOf([r.value for r in UnitOfSize])})
    weight_unit: str = field(
        metadata={"validate": OneOf([r.value for r in UnitOfWeight])}
    )
    type: str = field(metadata={"validate": OneOf([p.value for p in ProductTypes])})
    prices: Prices | None
    delivery_prices: DeliveryPrices | None


@dataclass
class ProductItem(BaseDataclass):
    id: int | None = field()
    product_id: int | None = field()
    name: str = field(metadata={"validate": Length(max=150)})
    cnt: Decimal = field()
    unit: str = field(metadata={"validate": OneOf([r.value for r in UnitOfCount])})


@dataclass
class FilesData(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    position: int = field(
        metadata={
            "strict": True,
        }
    )


@dataclass
class ProductRequest(ProductBaseDataclass):
    tags: list[int] = field(default_factory=list, metadata={"required": True})
    files: list[FilesData] = field(default_factory=list, metadata={"required": True})
    items: list[ProductItem] = field(default_factory=list, metadata={"required": True})


@dataclass
class Product(ProductBaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    owner_id: int = field(
        metadata={
            "strict": True,
        }
    )

    is_template: bool = field(default=False)
    images: list[Image] | None = field(default_factory=list)
    categories: list[Category] | None = field(default_factory=list)
    length: Decimal | None = field(default=None)
    height: Decimal | None = field(default=None)
    width: Decimal | None = field(default=None)
    weight: Decimal | None = field(default=None)
    min_flowers: Decimal | None = field(default=None)
    max_flowers: Decimal | None = field(default=None)
    compound: str | None = field(default=None)

    # items: list[ProductItem] | None = field(default_factory=list)

    @property
    def main_image(self) -> Image | None:
        if not self.images:
            return None
        for i in self.images:
            if i.position == 0:
                return i

    def __str__(self):
        return f"#{self.id} {self.name}"


@dataclass
class ProductResponse(SuccessResponse):
    result: Product = field()


@dataclass
class ProductsResponse(PagedResponse):
    result: list[Product] = field(default_factory=list, metadata={"required": True})


@dataclass
class FeaturedProductPrice(BaseDataclass):
    currency: str = field(metadata={"validate": Length(equal=3)})
    current: Decimal = field()
    old: Decimal | None = field()
    discount: Decimal = field()
    discount_percent: int = field()
    executor_discount_percent: int = field()
    cashback: int = field()


@dataclass
class FeaturedProductExecutor(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    name: str = field(metadata={"validate": Length(max=150)})
    url: str = field()
    price: FeaturedProductPrice = field()


@dataclass
class FeaturedProductCategory(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    parent_id: int | None = field(
        metadata={
            "strict": True,
        }
    )
    slug: str = field(metadata={"validate": Length(max=100, min=1)})
    name_ru: str = field(metadata={"validate": Length(max=50, min=1)}, default=None)


@dataclass
class FeaturedProduct(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    type: str = field(metadata={"validate": OneOf([p.value for p in ProductTypes])})
    slug: str = field(metadata={"validate": Length(max=150, min=1)})
    title: str = field(metadata={"validate": Length(max=150, min=1)})
    description: str | None = field(metadata={"validate": Length(max=1000)})
    height: Decimal | None
    width: Decimal | None
    properties: str = field(metadata={"validate": Length(max=20)})
    available_condition: Decimal
    color_id: int = field(metadata={"strict": True})
    color: str = field(metadata={"validate": Length(max=50)})
    florist_id: int = field(metadata={"strict": True})
    delivery_prices: DeliveryPrices
    compound: str | None = field(metadata={"validate": Length(max=1000)})
    prices: Prices
    categories: list[FeaturedProductCategory] | None = field(default_factory=list)
    images: list[Image] | None = field(default_factory=list)
    is_available: bool = field(default=True)
    min_flowers: int | None = field(default=None)
    max_flowers: int | None = field(default=None)
    avg_rating: float = field(default=0.0)


@dataclass
class FeaturedProductsResponse(PagedResponse):
    result: list[FeaturedProduct] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class SuccessFeaturedProductsResponse(SuccessResponse):
    result: list[FeaturedProduct] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class FeaturedProductResponse(SuccessResponse):
    result: FeaturedProduct = field()


@dataclass
class CityWithProductCnt(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    city: str = field(metadata={"validate": Length(max=150, min=1)})
    slug: str = field(metadata={"validate": Length(max=150, min=1)})
    product_cnt: int = field()


@dataclass
class CityWithProductCntResponse(SuccessResponse):
    result: list[CityWithProductCnt] = field()


@dataclass
class FeaturedProductsQuerystring(Querystring):
    delivery_date: date = field(default_factory=datetime.now().date)
    promo: str | None = field(default=None)
    currency: str = field(
        metadata={"validate": OneOf([r.value for r in Currency])}, default="rub"
    )


@dataclass
class IdsFeaturedProductsQuerystring(BaseDataclass):
    filters: str | None = field()  # фильтр
    promo: str | None = field()
    delivery_date: date = field(default_factory=datetime.now().date)
    delivery_time: int = field(default=-1)
    currency: str = field(
        metadata={"validate": OneOf([r.value for r in Currency])}, default="rub"
    )
    type: str | None = field


@dataclass
class PreferredExecutorQuerystring(BaseDataclass):
    promo: str | None = field()
    delivery_date: date = field(default_factory=datetime.now().date)
    currency: str = field(
        metadata={"validate": OneOf([r.value for r in Currency])}, default="rub"
    )


@dataclass
class PreferredExecutorResponse(SuccessResponse):
    result: FeaturedProductExecutor = field()


@dataclass
class TimePeriod(BaseDataclass):
    start: int = field(metadata={"strict": True})
    end: int = field(metadata={"strict": True})


@dataclass
class DeliveryTimePeriodResponse(SuccessResponse):
    result: TimePeriod | None = field()


@dataclass
class DeliveryTimePeriodRequest(BaseDataclass):
    city_id: int = field(metadata={"strict": True})
    delivery_date: date = field()
    ids: list[int] = field()
