from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.callbacks import (
    CallbackResponse,
    CallbackCreateRequest,
)
from ..presentations.error import ErrorResponse
from ..schemas.callbacks import CallbackResponseSchema


class CallbacksNamespace(Namespace):
    URL = "/callbacks/"

    @expectations(schema=CallbackResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CallbackCreateRequest, **kwargs
    ) -> (int, CallbackResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)
