from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.subscribe import (
    SubscribeResponse,
    SubscribeCreateRequest,
)
from ..presentations.error import ErrorResponse
from ..schemas.subscribe import SubscribeResponseSchema


class SubscribesNamespace(Namespace):
    URL = "/subscribes/"

    @expectations(schema=SubscribeResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: SubscribeCreateRequest, **kwargs
    ) -> (int, SubscribeResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)
