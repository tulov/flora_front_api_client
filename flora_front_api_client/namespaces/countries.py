from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.countries import SearchCountryResponse
from ..presentations.error import ErrorResponse
from ..schemas import (
    SearchCountriesResponseSchema
)


class CitiesNamespace(Namespace):
    URL = '/countries/'


    @expectations(schema=SearchCountriesResponseSchema)
    async def search(
        self, term: str = None, **kwargs
    ) -> (int, Union[SearchCountryResponse, ErrorResponse], RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'search/{term}'), **kwargs
        )
