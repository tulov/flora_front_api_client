from dataclasses import dataclass, field

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import PromoTypes, PromoWorkPeriod


@dataclass
class PromoCode(BaseDataclass):
    id: int = field(metadata={"strict": True,})
    code: str = field(metadata={"validate": Length(max=30)})
    discount: int =field()
    work_days: str = field(metadata={"validate": OneOf([p.value for p in PromoWorkPeriod])})
    type: str = field(metadata={"validate": OneOf([r.value for r in PromoTypes])})
    date_start: str | None = field(metadata={"validate": Length(max=15)})
    date_end: str | None = field(metadata={"validate": Length(max=15)})
    day_of_week: str | None = field(metadata={"validate": Length(max=15)})
    enabled: int = field()


@dataclass
class PromoCodeResponse(SuccessResponse):
    result: PromoCode = field()


@dataclass
class PromoCodesResponse(PagedResponse):
    result: list[PromoCode] = field(default_factory=list, metadata={"required": True})
