from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, SuccessResponse
from ..presentations.callbacks import (
    CallbackResponse,
    CallbacksResponse,
    CallbackCreateRequest,
    CallbackUpdateRequest,
)
from ..presentations.error import ErrorResponse
from ..schemas import SuccessResponseSchema
from ..schemas.callbacks import CallbackResponseSchema, CallbacksResponseSchema


class CallbacksNamespace(Namespace):
    URL = "/callbacks/"

    @expectations(schema=CallbackResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CallbackCreateRequest, **kwargs
    ) -> (int, CallbackResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=CallbacksResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, CallbacksResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=CallbackResponseSchema)
    async def update(
        self, id_: int, body: CallbackUpdateRequest, **kwargs
    ) -> (int, CallbackResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=id_), json=body.as_dict(), **kwargs
        )

    @expectations(schema=SuccessResponseSchema)
    async def remove(
        self, id_: int, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._delete(self.build_url(postfix_url=id_), **kwargs)
