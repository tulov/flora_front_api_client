from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.slider import (
    SliderResponse, SliderItemRequest, SliderItemResponse
)
from ..presentations.base import WithFieldsQuerystring, Querystring, SuccessResponse
from ..presentations.error import ErrorResponse
from ..schemas import SliderResponseSchema, SliderItemResponseSchema, SuccessResponseSchema
from ..namespaces.base import Namespace


class SliderItemsNamespace(Namespace):
    URL = '/slider-items/'

    @expectations(schema=SliderResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[SliderResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SliderItemResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: SliderItemRequest, **kwargs
    ) -> (int, Union[SliderItemResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=SliderItemResponseSchema)
    async def update(
        self, id_: int, data: SliderItemRequest, **kwargs
    ) -> (int, Union[SliderItemResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_),
                               json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def up(
        self, id_: int, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse], RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=f"{id_}/up"),
                               json={}, **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def down(
        self, id_: int, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse], RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=f"{id_}/down"),
                               json={}, **kwargs)

    @expectations(schema=SliderItemResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[SliderItemResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)
