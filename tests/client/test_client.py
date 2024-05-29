from http import HTTPStatus

import aiobreaker
import pytest
from aiohttp import ClientResponseError

from flora_front_api_client.client import FloraApiClient
from flora_front_api_client.presentations.auth import (
    AuthRequest,
    AuthResponse,
    RenewTokenResponse,
    RenewTokenRequest,
    SendRestoreAccessLinkRequest,
)
from flora_front_api_client.presentations.base import SuccessResponse
from flora_front_api_client.presentations.counters import CountersResponse
from flora_front_api_client.presentations.main import ApplicationInfoResponse
from flora_front_api_client.presentations.moderation import (
    RequestsForModerationResponse,
    RequestForModerationResponse,
    ModerationUpdateRequest,
)
from flora_front_api_client.presentations.users import (
    RegistrationUserData,
    User,
    ConfirmDataForAuthRequest,
    UsersResponse,
    ChangePasswordRequest,
)
from flora_front_api_client.utils.testing import mock


@mock("aiohttp.ClientSession.get", body={"version": "1.0.0", "name": "Flora Api"})
async def test_info(async_api_client):
    status, res, _ = await async_api_client.info.get()
    assert status == HTTPStatus.OK
    assert isinstance(res, ApplicationInfoResponse)


user_body = {
    "id": 1,
    "roles": ["user"],
    "registration_date": "2021-01-12T12:15:15",
    "name": "Lex",
    "discount": 0,
    "send_sms": True,
    "send_email": True,
    "language": "ru",
    "currency": "rub",
    "is_moderated": False,
    "banned": False,
    "data_for_auth": [
        {
            "id": 1,
            "service": "email",
            "is_checked": False,
            "value": "tulov.alex@gmail.com",
        },
        {"id": 2, "service": "phone", "is_checked": False, "value": "77077487125"},
    ],
}


@mock("aiohttp.ClientSession.post", body=user_body, status=HTTPStatus.CREATED)
async def test_registration_user(async_api_client):
    data = RegistrationUserData(
        "cbvcbv", "77077487125", "tulov.alex@gmail.com", "lex", "ru", "rub", True, True
    )
    status, res, _ = await async_api_client.users.register(data)
    assert status == HTTPStatus.CREATED
    assert isinstance(res, User)


user_data = {
    "id": 2,
    "roles": ["user", "partner"],
    "registration_date": "2021-01-12T12:15:15",
    "name": "Lex",
    "discount": 0,
    "send_sms": True,
    "send_email": True,
    "language": "ru",
    "currency": "rub",
    "is_moderated": False,
    "banned": False,
    "data_for_auth": [
        {
            "id": 1,
            "service": "email",
            "is_checked": False,
            "value": "tulov.alex@gmail.com",
        },
        {"id": 2, "service": "phone", "is_checked": False, "value": "77077487125"},
    ],
}


@mock("aiohttp.ClientSession.post", body=user_data, status=HTTPStatus.CREATED)
async def test_registration_partner(async_api_client):
    data = RegistrationUserData(
        "cbvcbv", "77077487125", "tulov.alex@gmail.com", "lex", "ru", "rub", True, True
    )
    status, res, _ = await async_api_client.partners.register(data)
    assert status == HTTPStatus.CREATED
    assert isinstance(res, User)


@mock(
    "aiohttp.ClientSession.post",
    body={"user": user_data, "token": "token", "long_token": "long_token"},
    status=HTTPStatus.OK,
)
async def test_auth(async_api_client):
    data = AuthRequest("77077487125", "cbvcbv")
    status, res, _ = await async_api_client.auth.authenticate(data)
    assert status == HTTPStatus.OK
    assert isinstance(res, AuthResponse)


@mock(
    "aiohttp.ClientSession.post",
    body={"token": "token", "long_token": "long_token"},
    status=HTTPStatus.OK,
)
async def test_renew_tokens(async_api_client):
    data = RenewTokenRequest("xxxxxxxxxxxxxxxxxxxxxxxxx")
    status, res, _ = await async_api_client.auth.renew(data)
    assert status == HTTPStatus.OK
    assert isinstance(res, RenewTokenResponse)


@mock(
    "aiohttp.ClientSession.post",
    body={
        "success": True,
    },
    status=HTTPStatus.OK,
)
async def test_send_restore_access_link(async_api_client):
    data = SendRestoreAccessLinkRequest(auth_key="test@test.loc")
    status, res, _ = await async_api_client.auth.send_restore_access_link(data)
    assert status == HTTPStatus.OK
    assert isinstance(res, SuccessResponse)


@mock(
    "aiohttp.ClientSession.put",
    body={
        "success": True,
    },
    status=HTTPStatus.OK,
)
async def test_auth_data_confirm(async_api_client):
    data = ConfirmDataForAuthRequest("0123")
    status, res, _ = await async_api_client.data_for_auth.confirm(1, data)
    assert status == HTTPStatus.OK
    assert isinstance(res, SuccessResponse)


@mock(
    "aiohttp.ClientSession.put",
    body={
        "success": True,
    },
    status=HTTPStatus.OK,
)
async def test_auth_data_resend(async_api_client):
    status, res, _ = await async_api_client.data_for_auth.resend(1)
    assert status == HTTPStatus.OK
    assert isinstance(res, SuccessResponse)


@mock("aiohttp.ClientSession.get", body=user_body, status=HTTPStatus.OK)
async def test_get_user(async_api_client):
    status, res, _ = await async_api_client.users.get(1)
    assert status == HTTPStatus.OK
    assert isinstance(res, User)


@mock(
    "aiohttp.ClientSession.get",
    body={
        "success": True,
        "result": [user_body],
        "pager": {"page": 1, "per_page": 10, "count_pages": 1},
    },
    status=HTTPStatus.OK,
)
async def test_all_user(async_api_client):
    status, res, _ = await async_api_client.users.all()
    assert status == HTTPStatus.OK
    assert isinstance(res, UsersResponse)


@mock(
    "aiohttp.ClientSession.get",
    body={
        "success": True,
        "result": [
            {
                "id": 1,
                "action": "user_registration",
                "date_added": "2021-01-12T12:15:15",
                "data": '{"test": "one"}',
                "user_id": 5,
            }
        ],
        "pager": {"page": 1, "per_page": 10, "count_pages": 1},
    },
    status=HTTPStatus.OK,
)
async def test_all_requests_for_moderation(async_api_client):
    status, res, _ = await async_api_client.moderation.all()
    assert status == HTTPStatus.OK
    assert isinstance(res, RequestsForModerationResponse)


@mock(
    "aiohttp.ClientSession.get",
    body={
        "success": True,
        "result": {
            "id": 1,
            "action": "user_registration",
            "date_added": "2021-01-12T12:15:15",
            "data": '{"test": "one"}',
            "user_id": 5,
        },
    },
    status=HTTPStatus.OK,
)
async def test_get_request_for_moderation(async_api_client):
    status, res, _ = await async_api_client.moderation.get(1)
    assert status == HTTPStatus.OK
    assert isinstance(res, RequestForModerationResponse)


@mock(
    "aiohttp.ClientSession.put",
    body={
        "success": True,
        "result": {
            "id": 1,
            "action": "user_registration",
            "date_added": "2021-01-12T12:15:15",
            "data": '{"test": "one"}',
            "user_id": 5,
        },
    },
    status=HTTPStatus.OK,
)
async def test_update_request_for_moderation(async_api_client):
    d = ModerationUpdateRequest("denied", "reason to denied")
    status, res, _ = await async_api_client.moderation.update(1, d)
    assert status == HTTPStatus.OK
    assert isinstance(res, RequestForModerationResponse)


@mock(
    "aiohttp.ClientSession.get",
    body={"success": True, "result": {"moderate": 5}},
    status=HTTPStatus.OK,
)
async def test_get_counters(async_api_client):
    status, res, _ = await async_api_client.counters.get()
    assert status == HTTPStatus.OK
    assert isinstance(res, CountersResponse)


@mock(
    "aiohttp.ClientSession.put",
    body={
        "success": True,
    },
    status=HTTPStatus.OK,
)
async def test_change_password(async_api_client):
    d = ChangePasswordRequest(old_password="cbvcbv", new_password="testtest")
    status, res, _ = await async_api_client.users.change_password(1, d)
    assert status == HTTPStatus.OK
    assert isinstance(res, SuccessResponse)


@pytest.mark.asyncio
async def test_circuit_breaker(fake_namespace):
    errors = []
    for i in range(10):
        try:
            await fake_namespace.run_with_status(500)
        except Exception as e:
            errors.append(e)
    breaker_opened = False
    for e in errors:
        if isinstance(e, aiobreaker.CircuitBreakerError):
            breaker_opened = True
        if breaker_opened:
            assert isinstance(e, aiobreaker.CircuitBreakerError)
        else:
            assert isinstance(e, ClientResponseError)
