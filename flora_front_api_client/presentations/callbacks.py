from datetime import datetime
from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse
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
    updated_at: datetime = field()
    comment: str | None = field(metadata={"validate": Length(max=1000)}, default=None)

    def __hash__(self):
        return hash(self.id) if self.id else hash(self.phone)


@dataclass
class CallbackCreateRequest(BaseDataclass):
    phone: str = field(metadata={"validate": Phone()})


@dataclass
class CallbackUpdateRequest(BaseDataclass):
    comment: str = field(metadata={"validate": Length(max=1000)})


@dataclass
class CallbackResponse(SuccessResponse):
    result: Callback = field()


@dataclass
class CallbacksResponse(PagedResponse):
    result: list[Callback] = field(default_factory=list, metadata={"required": True})
