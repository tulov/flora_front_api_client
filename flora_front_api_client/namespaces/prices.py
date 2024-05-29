from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, SuccessResponse
from ..presentations.prices import (
    PricesResponse, PricesRequest, PricesCurrentResponse,
    PricesCurrentQuerystring
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    PricesResponseSchema, SuccessResponseSchema, PricesCurrentResponseSchema,
)
from ..namespaces.base import Namespace


class PricesNamespace(Namespace):
    URL = '/prices/'

    @expectations(schema=PricesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[PricesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def set(
        self, data: PricesRequest, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse], RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=PricesCurrentResponseSchema)
    async def current(
        self, query_params: PricesCurrentQuerystring = None, **kwargs
    ) -> (int, Union[PricesCurrentResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(
            query_params, postfix_url="current/"), **kwargs)
