from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.subscribe import (
    SubscribeResponse,
    SubscribeCreateRequest,
    SubscribeConfirmRequest,
)
from ..presentations.base import SuccessResponse
from ..presentations.error import ErrorResponse
from ..schemas.subscribe import SubscribeResponseSchema
from ..schemas import SuccessResponseSchema


class SubscribesNamespace(Namespace):
    URL = "/subscribes/"

    @expectations(schema=SubscribeResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: SubscribeCreateRequest, **kwargs
    ) -> (int, SubscribeResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def confirm(
        self, id_: int, data: SubscribeConfirmRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}/confirm"), json=data.as_dict(), **kwargs
        )
