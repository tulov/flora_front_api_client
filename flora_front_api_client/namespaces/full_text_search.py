from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring
from ..presentations.error import ErrorResponse
from ..presentations.full_text_search import (
    ProductFullTextSearchRequest,
    ProductFullTextSearchResponse,
)
from ..schemas.full_text_search import ProductFullTextSearchResponseSchema


class FullTextSearchNamespace(Namespace):
    URL = "/full-text-search/"

    @expectations(schema=ProductFullTextSearchResponseSchema)
    async def products(
        self,
        data: ProductFullTextSearchRequest,
        query_params: Querystring = None,
        **kwargs
    ) -> (int, ProductFullTextSearchResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(query_params, postfix_url="products/"),
            json=data.as_dict(),
            **kwargs
        )
