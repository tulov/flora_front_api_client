from datetime import datetime
from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass
from .validates import Phone


@dataclass
class Callback(BaseDataclass):
    id: int | None = field(
        metadata={
            "strict": True,
        }
    )
    phone: str = field(metadata={"validate": Phone()})
    created_at: datetime = field()

    def __hash__(self):
        return hash(self.id) if self.id else hash(self.phone)


@dataclass
class CallbackCreateRequest(BaseDataclass):
    name: str = field(metadata={"validate": Length(max=150)})
    phone: str = field(metadata={"validate": Phone()})
    city_id: int = field(
        metadata={
            "strict": True,
        }
    )
    language: str = field(metadata={"validate": Length(equal=2)})
    currency: str = field(metadata={"validate": Length(equal=3)})
    user_id: int | None = field(
        metadata={
            "strict": True,
        },
        default=None,
    )
    ip: str = field(metadata={"validate": Length(max=100)}, default="")


@dataclass
class CallbackResponse(SuccessResponse):
    result: Callback = field()
