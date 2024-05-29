from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.counters import CountersResponse
from ..presentations.error import ErrorResponse
from ..schemas import CountersResponseSchema
from ..namespaces.base import Namespace


class CountersNamespace(Namespace):
    URL = '/counters/'

    @expectations(schema=CountersResponseSchema)
    async def get(
        self, **kwargs
    ) -> (int, Union[CountersResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.URL, **kwargs)
