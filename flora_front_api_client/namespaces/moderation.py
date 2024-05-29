from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.moderation import (
    RequestsForModerationResponse, RequestForModerationResponse,
    ModerationUpdateRequest
)
from ..presentations.products import ProductsResponse, ProductResponse, \
    ProductRequest
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..schemas import (
    RequestsForModerationResponseSchema,
    RequestForModerationResponseSchema,
    ProductsResponseSchema, ProductResponseSchema, WithFieldsQuerystringSchema
)
from ..namespaces.base import Namespace


class ModerationNamespace(Namespace):
    URL = '/requests-for-moderation/'

    @expectations(schema=RequestsForModerationResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def all(
        self, query_params: Querystring = None,  **kwargs
    ) -> (int, Union[RequestsForModerationResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=RequestForModerationResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[RequestForModerationResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=RequestForModerationResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def update(
        self, id_: int, data: ModerationUpdateRequest, **kwargs
    ) -> (int, Union[RequestForModerationResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=id_), json=data.as_dict(), **kwargs)

    @expectations(schema=ProductsResponseSchema)
    async def products(
        self, query_params: Querystring = None,  **kwargs
    ) -> (int, Union[ProductsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, url="/moderation/products/"),
            **kwargs)

    @expectations(schema=ProductResponseSchema)
    async def product(
        self, id_: int, query_params: WithFieldsQuerystringSchema = None,
        **kwargs
    ) -> (int, Union[ProductResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, url="/moderation/products/",
                           postfix_url=id_),
            **kwargs)

    @expectations(schema=ProductResponseSchema)
    async def update_product(
        self, id_: int, data: ProductRequest, **kwargs
    ) -> (int, Union[ProductResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(url="/moderation/products/",
                                              postfix_url=id_),
                               json=data.as_dict(), **kwargs)
