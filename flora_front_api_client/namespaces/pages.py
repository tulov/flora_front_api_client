from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.pages import PageResponse
from ..schemas.pages import PageResponseSchema
from ..presentations.base import Querystring



class PagesNamespace(Namespace):
    URL = "/pages/"

    @expectations(schema=PageResponseSchema)
    async def get(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, PageResponse | ErrorResponse, RenewTokenResponse):
            return await self._get(self.build_url(query_params), **kwargs)
