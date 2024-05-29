from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.main import ApplicationInfoResponse
from ..schemas import ApplicationInfoResponseSchema
from ..namespaces.base import Namespace


class InfoNamespace(Namespace):
    URL = '/info/'

    @expectations(schema=ApplicationInfoResponseSchema)
    async def get(
        self, **kwargs
    ) -> (int, Union[ApplicationInfoResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.URL, **kwargs)
