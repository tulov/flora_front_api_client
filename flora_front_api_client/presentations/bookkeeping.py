from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any

from marshmallow.validate import Length, OneOf

from .base import BaseDataclass, SuccessResponse, PagedResponse
from .enums import PaymentTypes, Currency


@dataclass
class BookkeepingRow(BaseDataclass):
    id: int = field(metadata={"strict": True})
    created_at: datetime = field()
    user_id: int = field(metadata={"strict": True})
    amount: Decimal = field()
    currency: str = field(metadata={"validate": Length(equal=3)})
    type: str = field(metadata={"validate": OneOf([r.value for r in PaymentTypes])})
    order_id: int | None = field(metadata={"strict": True}, default=None)
    account_id: int | None = field(metadata={"strict": True}, default=None)
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class Summary(BaseDataclass):
    before: Decimal = field()
    accrual: Decimal = field()
    payout: Decimal = field()
    current: Decimal = field()


@dataclass
class SummaryRequest(BaseDataclass):
    start: datetime = field()
    end: datetime = field()
    user_id: int = field()


@dataclass
class SummaryResponse(SuccessResponse):
    result: Summary = field()


@dataclass
class EntriesResponse(PagedResponse):
    result: list[BookkeepingRow] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class BRow(BaseDataclass):
    action: str = field(metadata={"validate": OneOf(["plus", "minus"])})
    user_id: int = field()
    amount: Decimal = field()
    comment: str = field()
    currency: str = field(metadata={"validate": OneOf([r.value for r in Currency])})
    contract_id: int | None = field(default=None)


@dataclass
class CreateBookkeepingRowsRequest(BaseDataclass):
    rows: list[BRow] = field()
