from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.cities import (
    CitiesResponse, SearchCitiesResponse, CityResponse
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    CitiesResponseSchema, SearchCitiesResponseSchema, CityResponseSchema
)
from ..namespaces.base import Namespace


class CitiesNamespace(Namespace):
    URL = '/cities/'

    @expectations(schema=CitiesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[CitiesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SearchCitiesResponseSchema)
    async def search(
        self, term: str = None, **kwargs
    ) -> (int, Union[SearchCitiesResponse, ErrorResponse], RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'search/{term}'), **kwargs
        )

    @expectations(schema=CityResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[CityResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)
