
from dataclasses import dataclass, field

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .cities import Country


@dataclass
class CountryResponse(SuccessResponse):
    result: Country = field()


@dataclass
class CountryResponse(PagedResponse):
    result: list[Country] = field(default_factory=list, metadata={"required": True})


@dataclass
class SearchCountry(BaseDataclass):
    id: int = field(metadata={"strict": True})
    name: str = field()
    slug: str = field()


@dataclass
class SearchCountryResponse(SuccessResponse):
    result: list[SearchCountry] = field(default_factory=list, metadata={"required": True})
