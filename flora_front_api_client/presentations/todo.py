from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from marshmallow.validate import Length, OneOf

from .base import BaseDataclass, PagedResponse
from .enums import TodoStates, TodoTypes
from .users import Employee


@dataclass
class Todo(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    created_at: datetime = field()
    updated_at: datetime = field()
    type: str = field(
        metadata={
            "validate": OneOf([a.value for a in TodoTypes]),
        }
    )
    state: str = field(
        metadata={
            "validate": OneOf([a.value for a in TodoStates]),
        }
    )
    message: str = field(metadata={"validate": Length(max=1500)})
    order_id: int = field(
        metadata={
            "strict": True,
        }
    )
    user_id: int = field(
        metadata={
            "strict": True,
        }
    )
    employee_id: int | None = field(
        metadata={
            "strict": True,
        },
        default=None,
    )
    comments: str | None = field(metadata={"validate": Length(max=1500)}, default=None)
    data: Any = field(default_factory=dict)
    employee: Employee | None = field(default=None)


@dataclass
class TodosResponse(PagedResponse):
    result: list[Todo] = field(default_factory=list)
