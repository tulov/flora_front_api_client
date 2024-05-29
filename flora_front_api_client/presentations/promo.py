from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import PromoTypes


@dataclass
class PromoCode(BaseDataclass):
    code: str = field(metadata={"validate": Length(max=30)})
    type: str = field(metadata={"validate": OneOf([r.value for r in PromoTypes])})
    is_valid: bool = field()
    data: dict[str, Any] = field(default_factory=dict)
    created_at: datetime | None = field(default=None)

    def check(self) -> bool:
        if not self.is_valid:
            return False
        if "period" in self.data and self.data["period"]:
            cur_date = datetime.now().date()
            arr = self.data["period"].split(" - ")
            start = datetime.strptime(arr[0], "%d.%m.%Y").date()
            end = datetime.strptime(arr[1], "%d.%m.%Y").date()
            return start <= cur_date <= end
        return True


@dataclass
class PromoCodeResponse(SuccessResponse):
    result: PromoCode = field()


@dataclass
class PromoCodesResponse(PagedResponse):
    result: list[PromoCode] = field(default_factory=list, metadata={"required": True})
