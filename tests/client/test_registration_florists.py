from http import HTTPStatus

import pytest

from flora_front_api_client.client import FloraApiClient
from flora_front_api_client.presentations.users import RegistrationFloristData, User
from flora_front_api_client.utils.testing import mock


pytestmark = pytest.mark.asyncio


@pytest.fixture(autouse=True)
def enable_mock(monkeypatch):
    monkeypatch.setattr("flora_front_api_client.utils.testing.WITH_MOCK", True)


@pytest.fixture
def async_api_client():
    return FloraApiClient(
        app_id="test_app_id",
        app_key="test_private_key",
        host="http://0.0.0.0:8081",
        cloudinary_config_kwargs={},
    )


user_data = {
    "id": 2,
    "roles": ["user", "partner"],
    "registration_date": "2021-01-12T12:15:15",
    "name": "Flower Shop",
    "discount": 0,
    "feed_sms": True,
    "feed_news": True,
    "language": "ru",
    "currency": "rub",
    "percent_us": 20,
    "is_moderated": False,
    "banned": False,
    "data_for_auth": [
        {"id": 1, "service": "email", "is_checked": False, "value": "shop@example.com"},
        {"id": 2, "service": "phone", "is_checked": False, "value": "77771234567"},
    ],
}


@mock("aiohttp.ClientSession.post", body=user_data, status=HTTPStatus.CREATED)
async def test_registration_florist(async_api_client):
    data = RegistrationFloristData(
        company_name="Flower Shop",
        phone="+7 (777) 123-45-67",
        email="shop@example.com",
    )
    status, res, _ = await async_api_client.users.register_florist(data)
    assert status == HTTPStatus.CREATED
    assert isinstance(res, User)


@mock(
    "aiohttp.ClientSession.post",
    body={
        "error": {
            "code": "bad_request",
            "message": "Request validation has failed",
            "fields": {
                "phone": ["Укажите телефон или email."],
                "email": ["Укажите телефон или email."],
            },
        }
    },
    status=HTTPStatus.BAD_REQUEST,
)
async def test_registration_florist_validation_error(async_api_client):
    status, res, _ = await async_api_client.users.register_florist({})
    assert status == HTTPStatus.BAD_REQUEST
    assert res.error.fields["phone"] == ["Укажите телефон или email."]
