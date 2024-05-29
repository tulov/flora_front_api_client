from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal

from marshmallow import ValidationError
from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .cities import City
from .enums import ProgramAction, ProgramType
from .products import Product


@dataclass
class Program(BaseDataclass):
    id: int | None = field(
        metadata={
            "strict": True,
        }
    )
    partner_id: int = field(
        metadata={
            "strict": True,
        }
    )
    title: str = field(metadata={"validate": Length(max=100)})
    description: str | None = field()
    type: str = field(
        metadata={
            "validate": OneOf([r.value for r in ProgramType]),
        }
    )
    action: str = field(
        metadata={
            "validate": OneOf([r.value for r in ProgramAction]),
        }
    )
    value: Decimal = field()
    currency: str | None = field(metadata={"validate": Length(equal=3)})
    start: datetime | None = field()
    end: datetime | None = field()
    product_ids: list[int] = field(default_factory=list)
    geoname_ids: list[int] = field(default_factory=list)

    def __post_init__(self):
        if self.start and self.end and self.start > self.end:
            raise ValidationError("'Start' should be less then 'end'")


@dataclass
class ProgramDetail(Program):
    products: list[Product] | None = field(default_factory=list)
    cities: list[City] | None = field(default_factory=list)


@dataclass
class ProgramResponse(SuccessResponse):
    result: ProgramDetail = field()


@dataclass
class ProgramsResponse(PagedResponse):
    result: list[ProgramDetail] = field(
        default_factory=list, metadata={"required": True}
    )
