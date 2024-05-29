from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from marshmallow.validate import Length, OneOf

from .base import BaseDataclass, PagedResponse, SuccessResponse
from .enums import ModerationAction, ModerationResult
from .users import User


@dataclass
class RequestForModeration(BaseDataclass):
    id: int = field()
    action: str = field(
        metadata={
            "validate": OneOf([a.value for a in ModerationAction]),
        }
    )
    date_added: datetime = field()
    user_id: int = field()
    revision: int = field(
        metadata={
            "strict": True,
        }
    )
    data: Any = field(default_factory=dict)
    result: str | None = field(
        metadata={
            "validate": OneOf([r.value for r in ModerationResult]),
        },
        default=None,
    )
    date_result: datetime | None = field(default=None)
    admin_id: int | None = field(default=None)
    cause: str | None = field(metadata={"validate": Length(max=1500)}, default=None)
    user: User | None = field(default=None)
    admin: User | None = field(default=None)
    obj_id: int | None = field(default=None)


@dataclass
class RequestsForModerationResponse(PagedResponse):
    result: list[RequestForModeration] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class RequestForModerationResponse(SuccessResponse):
    result: RequestForModeration = field()


@dataclass
class ModerationUpdateRequest(BaseDataclass):
    result: str = field(
        metadata={
            "validate": OneOf([r.value for r in ModerationResult]),
        }
    )
    cause: str | None = field(metadata={"validate": Length(max=1500)})
    revision: int = field(
        metadata={
            "strict": True,
        }
    )
