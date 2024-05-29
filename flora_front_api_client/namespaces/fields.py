from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.fields import (
    FieldResponse, CreateFieldRequest, FieldsResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import FieldResponseSchema, FieldsResponseSchema
from ..namespaces.base import Namespace


class FieldsNamespace(Namespace):
    URL = '/fields/'

    @expectations(schema=FieldResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CreateFieldRequest, **kwargs
    ) -> (int, Union[FieldResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=FieldsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[FieldsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=FieldResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[FieldResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=FieldResponseSchema)
    async def update(
        self, id_: int, data: CreateFieldRequest, **kwargs
    ) -> (int, Union[FieldResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_),
                               json=data.as_dict(), **kwargs)
