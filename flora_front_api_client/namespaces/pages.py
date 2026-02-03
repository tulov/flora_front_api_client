from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.pages import PageResponse
from ..schemas.pages import PageResponseSchema


class PagesNamespace(Namespace):
    URL = "/pages/"

    @expectations(schema=PageResponseSchema)
    async def get(
        self, slug: str, **kwargs
    ) -> (int, PageResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(postfix_url=slug), **kwargs)
