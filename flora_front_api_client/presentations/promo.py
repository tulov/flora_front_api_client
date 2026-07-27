from dataclasses import dataclass, field
from datetime import datetime

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import PromoTypes, PromoWorkPeriod


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%d/%m")


def _parse_month_day(date_str: str) -> tuple[int, int]:
    parsed = parse_date(date_str)
    return parsed.month, parsed.day


def _is_within_annual_range(
    today: tuple[int, int], start: tuple[int, int], end: tuple[int, int]
) -> bool:
    if start <= end:
        return start <= today <= end
    return today >= start or today <= end

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


    def check(self, now: datetime | None = None) -> bool:
        if now is None:
            now = datetime.now()
        if not self.enabled:
            return False
        if self.work_days == "date":
            today = (now.month, now.day)
            start = _parse_month_day(self.date_start)
            end = _parse_month_day(self.date_end)
            if not _is_within_annual_range(today, start, end):
                return False
        elif self.work_days == "week":
            days = list(map(int, self.day_of_week.split(',')))
            current_day = now.weekday()
            return current_day in days
        return True

@dataclass
class PromoCodeResponse(SuccessResponse):
    result: PromoCode = field()


@dataclass
class PromoCodesResponse(PagedResponse):
    result: list[PromoCode] = field(default_factory=list, metadata={"required": True})
