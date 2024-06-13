from datetime import datetime
from dataclasses import dataclass, field

from marshmallow.validate import Length, Email

from .base import SuccessResponse, BaseDataclass


@dataclass
class Subscribe(BaseDataclass):
    id: int | None = field(
        metadata={
            "strict": True,
        }
    )
    email: str = field(metadata={"validate": Email()})
    created_at: datetime = field()

    def __hash__(self):
        return hash(self.id) if self.id else hash(self.email)


@dataclass
class SubscribeCreateRequest(BaseDataclass):
    email: str = field(metadata={"validate": Email()})
    language: str = field(metadata={"validate": Length(equal=2)})
    ip: str = field(metadata={"validate": Length(max=100)}, default="")


@dataclass
class SubscribeResponse(SuccessResponse):
    result: Subscribe = field()
