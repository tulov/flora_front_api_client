from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.seo import UrlQuerystring, SEOResponse
from ..schemas.seo import SEOResponseSchema


class SEONamespace(Namespace):
    URL = "/seo/"

    @expectations(schema=SEOResponseSchema)
    async def get(
        self, query_params: UrlQuerystring, **kwargs
    ) -> (int, SEOResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)
