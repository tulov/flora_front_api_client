from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring
from ..presentations.countries import SearchCountryResponse, CountryResponse
from ..presentations.error import ErrorResponse
from ..schemas.countries import CountriesResponseSchema
from ..schemas import (
    SearchCountriesResponseSchema
)


class CountriesNamespace(Namespace):
    URL = '/countries/'

    @expectations(schema=CountriesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[CountryResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SearchCountriesResponseSchema)
    async def search(
        self, term: str = None, **kwargs
    ) -> (int, Union[SearchCountryResponse, ErrorResponse], RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'search/{term}'), **kwargs
        )


    @expectations(schema=SearchCountriesResponseSchema)
    async def search(
        self, term: str = None, **kwargs
    ) -> (int, Union[SearchCountryResponse, ErrorResponse], RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'search/{term}'), **kwargs
        )
