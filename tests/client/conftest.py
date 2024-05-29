from datetime import timedelta

import pytest
import os

from aiobreaker import CircuitBreaker

from flora_front_api_client.auth.singer import Singer
from flora_front_api_client.client import FloraApiClient
from flora_front_api_client.namespaces.base import Namespace

API_SERVER_URL = os.environ.get("TEST_API_SERVER_URL", "http://0.0.0.0:8081")
PRIVATE_KEY = os.environ.get("TEST_API_PRIVATE_KEY", "")
PUBLIC_KEY = os.environ.get("TEST_API_PUBLIC_KEY", "")


@pytest.fixture
def async_api_client():
    return FloraApiClient(app_id=PUBLIC_KEY, app_key=PRIVATE_KEY, host=API_SERVER_URL)


class FakeNamespace(Namespace):
    async def run_with_status(self, status: int):
        return await self._get(f"/{status}")


@pytest.fixture
def fake_namespace():
    signer = Singer(private_key="test_private_key", public_key="test_app_id")
    breaker = CircuitBreaker(
        fail_max=3,
        timeout_duration=timedelta(minutes=1),
    )
    return FakeNamespace("https://httpbin.org", "/status", signer, breaker)
