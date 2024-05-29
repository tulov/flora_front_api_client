from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, SuccessResponse
from ..presentations.bookkeeping import (
    SummaryResponse,
    EntriesResponse,
    SummaryRequest,
    CreateBookkeepingRowsRequest,
)
from ..presentations.error import ErrorResponse
from ..schemas.bookkeeping import (
    BookkeepingSummaryResponseSchema,
    BookkeepingEntriesResponseSchema,
)
from ..schemas import SuccessResponseSchema


class BookkeepingNamespace(Namespace):
    URL = "/bookkeeping/"

    @expectations(schema=BookkeepingEntriesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, EntriesResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=BookkeepingSummaryResponseSchema)
    async def summary(
        self, query_params: SummaryRequest, **kwargs
    ) -> (int, SummaryResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url="summary/"), **kwargs
        )

    @expectations(schema=SuccessResponseSchema)
    async def create(
        self, data: CreateBookkeepingRowsRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)
