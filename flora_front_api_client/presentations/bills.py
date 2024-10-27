from dataclasses import dataclass, field
from datetime import datetime, date
from decimal import Decimal
from typing import Any

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .images import Image


@dataclass
class BillOrderDataItem(BaseDataclass):
    image: Image = field()
    cnt: int = field(metadata={"strict": True})
    name: str = field()
    old_price: Decimal = field()
    price: Decimal = field()
    height: Decimal = field()
    width: Decimal = field()
    product_id: int = field()


@dataclass
class BillOrderData(BaseDataclass):
    id: int = field(metadata={"strict": True})
    city_id: int = field(metadata={"strict": True})
    delivery_date: date = field()
    delivery_time: int = field()
    amount: Decimal = field()
    currency: str = field(metadata={"validate": Length(equal=3)})
    state: str = field()
    city_name: str = field()
    receiver_name: str = field(metadata={"validate": Length(max=150)})
    receiver_phone: str = field(metadata={"validate": Length(max=100)})
    delivery_address: str = field(metadata={"validate": Length(max=1000)})
    card_text: str = field(metadata={"validate": Length(max=1000)})
    items: list[BillOrderDataItem] | None = field(default_factory=list)


@dataclass
class BillUserContact(BaseDataclass):
    service: str = field()
    auth_key: str = field()


@dataclass
class Bill(BaseDataclass):
    id: int = field(metadata={"strict": True})
    guid: str = field()
    created_at: datetime = field()
    user_id: int = field(metadata={"strict": True})
    order_id: int = field(metadata={"strict": True})
    amount: Decimal = field()
    currency: str = field(metadata={"validate": Length(equal=3)})
    is_paid: bool = field()
    comment: str | None = field(default=None)
    parent_id: int | None = field(default=None)
    order_data: BillOrderData | None = field(default=None)
    user_contacts: list[BillUserContact] | None = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)

    def _get_contact(self, contact_type: str) -> str:
        if not self.user_contacts:
            return ""
        for c in self.user_contacts:
            if c.service == contact_type:
                return c.auth_key
        return ""

    @property
    def user_phone(self) -> str:
        return self._get_contact("phone")

    @property
    def user_email(self) -> str:
        return self._get_contact("email")


@dataclass
class BillResponse(SuccessResponse):
    result: Bill = field()


@dataclass
class BillsResponse(PagedResponse):
    result: list[Bill] = field(default_factory=list, metadata={"required": True})


@dataclass
class BillPayRequest(BaseDataclass):
    pass


@dataclass
class CloudpaymentsBillPayRequest(BillPayRequest):
    cryptogram: str = field()
    holder_name: str = field()


@dataclass
class CloudpaymentsBillAfter3dRequest(BillPayRequest):
    TransactionId: int = field()
    PaRes: str = field()


@dataclass
class File(BaseDataclass):
    content: str = field()
    file_name: str = field()
    file_type: str = field()


@dataclass
class BillPDFResponse(SuccessResponse):
    result: File = field()


@dataclass
class PayRussianFederationBillQuerystring(BaseDataclass):
    id: int = field()  # идентификатор заказа со стороны paygine
    operation: int = field()  # идентификатор операции на стороне paygine
    reference: int = field()  # идентификатор заказа на стороне флоры
    error: int | None = field()  # номер ошибки, если она возникла
