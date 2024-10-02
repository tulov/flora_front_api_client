from dataclasses import dataclass, field
from datetime import datetime

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import PromoTypes, PromoWorkPeriod


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%d/%m")

@dataclass
class PromoCode(BaseDataclass):
    id: int = field(metadata={"strict": True,})
    code: str = field(metadata={"validate": Length(max=30)})
    discount: int = field()
    day_of_week: str | None = field(metadata={"validate": Length(max=15)})
    work_days: str = field(metadata={"validate": OneOf([p.value for p in PromoWorkPeriod])})
    enabled: int = field()
    promo_type: int = field()
    date_start: str | None = field(metadata={"validate": Length(max=15)}, default=None)
    date_end: str | None = field(metadata={"validate": Length(max=15)}, default=None)


    def check(self) -> bool:
        if not self.enabled:
            return False
        if self.work_days == "date":
            if not parse_date(self.date_start) <= datetime.now() <= parse_date(self.date_end):
                return False
        elif self.work_days == "week":
            days = list(map(int, self.day_of_week.split(',')))
            current_day = datetime.now().weekday()
            return current_day in days
        return True

@dataclass
class PromoCodeResponse(SuccessResponse):
    result: PromoCode = field()


@dataclass
class PromoCodesResponse(PagedResponse):
    result: list[PromoCode] = field(default_factory=list, metadata={"required": True})
