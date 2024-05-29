from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.programs import (
    ProgramResponse, ProgramsResponse, Program, ProgramDetail
)
from ..presentations.error import ErrorResponse
from ..schemas import ProgramResponseSchema, ProgramsResponseSchema
from ..namespaces.base import Namespace


class ProgramsNamespace(Namespace):
    URL = '/programs/'

    @expectations(schema=ProgramResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: Program, **kwargs
    ) -> (int, Union[ProgramResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=ProgramsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[ProgramsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=ProgramResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[ProgramResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=ProgramResponseSchema)
    async def update(
        self, id_: int, data: Program, **kwargs
    ) -> (int, Union[ProgramResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_),
                               json=data.as_dict(), **kwargs)
