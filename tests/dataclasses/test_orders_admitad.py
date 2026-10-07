import pytest
from marshmallow import ValidationError

from flora_front_api_client.schemas.orders import CreateOrderRequestSchema


def _payload(**overrides):
    payload = {
        "guid": "order-guid",
        "delivery_date": "2026-08-20",
        "city_id": 2800,
        "delivery_time": -1,
        "receiver_name": "Alice",
        "receiver_phone": "+77000000000",
        "delivery_address": "Address",
        "card_text": "",
        "promo_code": None,
        "user_sum": "100.00",
        "currency": "rub",
        "payment_method": "cloudpayments_ru",
        "products": [{"product_id": "55", "count": 1}],
    }
    payload.update(overrides)
    return payload


def test_create_order_request_keeps_admitad_uid_optional_for_organic_orders():
    loaded = CreateOrderRequestSchema().load(_payload())

    assert loaded.admitad_uid is None


def test_create_order_request_accepts_nullable_admitad_uid():
    loaded = CreateOrderRequestSchema().load(_payload(admitad_uid=None))

    assert loaded.admitad_uid is None


def test_create_order_request_accepts_admitad_uid():
    loaded = CreateOrderRequestSchema().load(
        _payload(admitad_uid="03b374fa9c2f"),
    )

    assert loaded.admitad_uid == "03b374fa9c2f"


def test_create_order_request_rejects_overlong_admitad_uid():
    with pytest.raises(ValidationError):
        CreateOrderRequestSchema().load(_payload(admitad_uid="x" * 2049))
