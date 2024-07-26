from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from marshmallow.validate import Length, OneOf, Range

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .bills import Bill
from .cities import City, Country
from .enums import OrderState, OrderTypes
from .images import Image
from .products import Product
from .users import User


@dataclass
class OrderProduct(BaseDataclass):
    product_id: int = field(metadata={"strict": True})
    count: int = field(metadata={"strict": True})


@dataclass
class OrderItem(OrderProduct):
    order_id: int = field(metadata={"strict": True})
    product_id: int = field(metadata={"strict": True})
    product_parent_id: int = field(metadata={"strict": True})
    count: int = field(metadata={"strict": True})
    price: Decimal = field()
    discount: int = field(metadata={"strict": True})
    discount_sum: Decimal = field(metadata={"strict": True})
    object: str = field(metadata={"strict": True})
    flower_count: int = field(metadata={"strict": True})
    product: Product | None = field(default_factory=list)


@dataclass
class OrderCommentBase(BaseDataclass):
    comment: str = field(metadata={"validate": Length(max=300, min=1)})


@dataclass
class OrderComment(OrderCommentBase):
    id: int = field(metadata={"strict": True})
    created_at: datetime = field()
    user_id: int | None = field(metadata={"strict": True})
    order_id: int = field(metadata={"strict": True})
    user_name: str | None = field()


@dataclass
class OrderInvoices(BaseDataclass):
    key: str | None = field(metadata={"validate": Length(max=64)})
    cost: Decimal = field()
    created: int = field()
    order_id: int = field(metadata={"strict": True})


@dataclass
class Answer(BaseDataclass):
    rating: int | None = field(
        metadata={"strict": True, "validate": Range(min=1, max=5)}, default=None
    )
    id: int | None = field(metadata={"strict": True}, default=None)
    created_at: datetime = field(default_factory=datetime.utcnow)
    txt: str | None = field(default=None)
    is_checked: bool = field(default=False)
    is_publish: bool = field(default=False)
    data: Any = field(default_factory=dict)
    city: City | None = field(default=None)
    user: User | None = field(default=None)


@dataclass
class Order(BaseDataclass):
    id: int = field(metadata={"strict": True})
    app_id: int = field(metadata={"strict": True})
    type: str = field(metadata={"validate": OneOf([r.value for r in OrderTypes])})
    currency_id: int | None = field(metadata={"strict": True})
    user_id: int | None = field(metadata={"strict": True})
    summ: Decimal | None = field()
    summ_manual: Decimal | None = field()
    summ_manual_rub: Decimal | None = field()
    date_order: int = field()
    date_delive: int = field()
    time: int = field()
    photo: int = field()
    photo_loaded: int = field()
    photo_before_loaded: int = field()
    promocode: str = field(metadata={"validate": Length(max=50)})
    receiver_city_id: int = field(metadata={"strict": True})
    receiver_country_id: int = field(metadata={"strict": True})
    receiver_city: str = field(metadata={"validate": Length(max=150)})
    receiver_country: str = field(metadata={"validate": Length(max=150)})
    receiver_name: str = field(metadata={"validate": Length(max=150)})
    receiver_address: str = field(metadata={"validate": Length(max=1000)})
    receiver_phone: str = field(metadata={"validate": Length(max=100)})
    receiver_phone_clear: str = field(metadata={"validate": Length(max=20)})
    sender_name: str = field(metadata={"validate": Length(max=150)})
    sender_email: str = field(metadata={"validate": Length(max=150)})
    sender_phone: str = field(metadata={"validate": Length(max=100)})
    sender_phone_clear: str = field(metadata={"validate": Length(max=20)})
    sender_country: str = field(metadata={"validate": Length(max=50)})
    sender_city: str = field(metadata={"validate": Length(max=50)})
    sender_ip: str = field(metadata={"validate": Length(max=15)})
    language: str = field(metadata={"validate": Length(max=5)})
    discount: int | None = field()
    status: str = field(metadata={"validate": OneOf([r.value for r in OrderState])})
    status_changed: int | None = field()
    florist_id: int = field(metadata={"strict": True})
    creator_id: int = field(metadata={"strict": True})
    delivery_cost: Decimal | None = field()
    total_rub: Decimal | None = field()
    wishes: str | None = field(default='')
    currency: str | None = field(default='rub')
    tech: str | None = field(default=None)
    items: list[OrderItem] | None = field(default_factory=list)
    order_invoices: list[OrderInvoices] | None = field(default_factory=list)


    @property
    def not_send_photos(self) -> list[Image]:
        return [
            p
            for p in self.photos_before_delivery
            if not p.data.get("is_sender_send", False)
        ]

    @property
    def has_sent_photos(self) -> bool:
        if not self.is_complicated:
            return (
                len(
                    list(
                        filter(
                            lambda p: p.data.get("is_sender_send", False),
                            self.photos_before_delivery,
                        )
                    )
                )
                > 0
            )
        has_children = True
        for c in self.children:
            has_children = (
                len(
                    list(
                        filter(
                            lambda p: p.data.get("is_sender_send", False),
                            c.photos_before_delivery,
                        )
                    )
                )
                > 0
            )
            if not has_children:
                break
        return has_children

    def get_max_time_for_accept(self) -> datetime | None:
        return self._max_time_for_accept


@dataclass
class CreateOrderRequest(BaseDataclass):
    guid: str = field()
    delivery_date: date = field()
    city_id: int = field(metadata={"strict": True})
    delivery_time: int = field(metadata={"strict": True})
    receiver_name: str = field(metadata={"validate": Length(max=150)})
    receiver_phone: str = field(metadata={"validate": Length(max=100)})
    delivery_address: str = field(metadata={"validate": Length(max=1000)})
    card_text: str = field(metadata={"validate": Length(max=1000)})
    promo_code: str | None = field()
    user_sum: Decimal = field()
    currency: str = field(metadata={"validate": Length(equal=3)})
    take_photo_with_receiver: bool = (field(default=False),)
    products: list[OrderProduct] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class OrderResponse(SuccessResponse):
    result: Order = field()


@dataclass
class OrderCommentRequest(OrderCommentBase):
    revision: int = field(metadata={"strict": True})


@dataclass
class OrderCommentResponse(SuccessResponse):
    result: OrderComment = field()


@dataclass
class OrderBillResponse(SuccessResponse):
    result: Bill = field()


@dataclass
class OrderBillRequest(BaseDataclass):
    amount: Decimal = field()
    comment: str | None = field(metadata={"validate": Length(max=150)})
    revision: int = field(metadata={"strict": True})


@dataclass
class OrdersResponse(PagedResponse):
    result: list[Order] = field(default_factory=list, metadata={"required": True})


@dataclass
class AfterRejectRequestBody(BaseDataclass):
    provider_id: int = field(metadata={"strict": True})
    hash: str = field(metadata={"validate": Length(equal=15)})


@dataclass
class OrderAnswerResponse(SuccessResponse):
    result: list[Answer] = field(default_factory=list, metadata={"required": True})


@dataclass
class AnswerResponse(SuccessResponse):
    result: Answer = field()


@dataclass
class AnswersResponse(PagedResponse):
    result: list[Answer] = field(default_factory=list, metadata={"required": True})


@dataclass
class CancelOrderCalculation(BaseDataclass):
    order_id: int = field()
    return_sum: Decimal = field()
    state: str = field()
    payed_sum: Decimal = field()
    revision: int = field()


@dataclass
class CancelOrderCalculationResponse(SuccessResponse):
    result: CancelOrderCalculation = field()
