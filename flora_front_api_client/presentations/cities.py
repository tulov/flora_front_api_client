# from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse


@dataclass
class Continent(BaseDataclass):
    id: int = field(metadata={"strict": True})
    iso: str = field(metadata={"validate": Length(equal=2)})
    name_ru: str = field(metadata={"validate": Length(max=30)})
    slug: str = field(metadata={"validate": Length(max=100)})


@dataclass
class Subcontinent(BaseDataclass):
    id: int = field(metadata={"strict": True})
    continent_id: int = field(metadata={"strict": True})
    iso: str = field(metadata={"validate": Length(equal=3)})
    name_ru: str = field(metadata={"validate": Length(max=30)})
    slug: str = field(metadata={"validate": Length(max=100)})
    continent: Continent | None = field()


@dataclass
class Country(BaseDataclass):
    id: int = field(metadata={"strict": True})
    subcontinent_id: int = field(metadata={"strict": True})
    iso: str = field(metadata={"validate": Length(equal=2)})
    populations: int = field(
        metadata={
            "strict": True,
        }
    )
    name_ru: str = field(metadata={"validate": Length(max=30)})
    slug: str = field(metadata={"validate": Length(max=100)})
    capital_id: int | None = field(metadata={"strict": True})
    subcontinent: Subcontinent | None = field()


@dataclass
class Region(BaseDataclass):
    id: int = field(metadata={"strict": True})
    country_id: int = field(metadata={"strict": True})
    iso: str = field(metadata={"validate": Length(max=4)})
    populations: int | None = field(
        metadata={
            "strict": True,
        }
    )
    name_ru: str = field(metadata={"validate": Length(max=50)})
    slug: str = field(metadata={"validate": Length(max=100)})
    country: Country | None = field()


@dataclass
class DeliveryData(BaseDataclass):
    currency: str = field(metadata={"validate": Length(equal=3)})
    price: Decimal = field()
    time: int = field()
    time_unit: str = field()


@dataclass
class City(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    country_id: int = field(metadata={"strict": True})
    region_id: int | None = field(metadata={"strict": True})
    parent_city_id: int | None = field(metadata={"strict": True})
    lat: Decimal = field()
    lng: Decimal = field()
    name_ru: str = field(metadata={"validate": Length(max=50)})
    slug: str = field(metadata={"validate": Length(max=100)})
    gmt: Decimal | None = field()
    timezone: str | None = field(metadata={"validate": Length(max=100)})
    delivery: DeliveryData | None = field()
    country: Country | None = field()
    parent_city: Any | None = field()
    region: Region | None = field()

    def __str__(self):
        s = self.name_ru
        if self.parent_city:
            if type(self.parent_city) == dict:
                s += ", " + self.parent_city["name_ru"]
            else:
                s += ", " + self.parent_city.name_ru
        if self.region and self.region.name_ru not in self.name_ru:
            s += ", " + self.region.name_ru
        if self.country:
            s += ", " + self.country.name_ru
        return s


@dataclass
class CityResponse(SuccessResponse):
    result: City = field()


@dataclass
class CitiesResponse(PagedResponse):
    result: list[City] = field(default_factory=list, metadata={"required": True})


@dataclass
class SearchCity(BaseDataclass):
    id: int = field(metadata={"strict": True})
    name: str = field()
    slug: str = field()


@dataclass
class SearchCitiesResponse(SuccessResponse):
    result: list[SearchCity] = field(default_factory=list, metadata={"required": True})
