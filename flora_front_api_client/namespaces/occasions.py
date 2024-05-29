from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, SuccessResponse
from ..presentations.congratulations import (
    OccasionsResponse,
    OccasionResponse,
    Occasion,
    Congratulation,
    CongratulationResponse,
    SortRequest,
)
from ..presentations.error import ErrorResponse
from ..schemas.congratulations import (
    OccasionResponseSchema,
    OccasionsResponseSchema,
    CongratulationResponseSchema,
)
from ..schemas import SuccessResponseSchema


class OccasionsNamespace(Namespace):
    URL = "/occasions/"

    @expectations(schema=OccasionResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: Occasion, **kwargs
    ) -> (int, OccasionResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=OccasionResponseSchema)
    async def update(
        self, data: Occasion, **kwargs
    ) -> (int, OccasionResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=data.id), json=data.as_dict(), **kwargs
        )

    @expectations(schema=SuccessResponseSchema)
    async def sort(
        self, data: SortRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url="sort/"), json=data.as_dict(), **kwargs
        )

    @expectations(schema=SuccessResponseSchema)
    async def sort_congratulations(
        self, occasion_id: int, data: SortRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{occasion_id}/sort-congratulations/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=OccasionsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, OccasionsResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=CongratulationResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create_congratulation(
        self, data: Congratulation, **kwargs
    ) -> (int, CongratulationResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{data.occasion_id}/congratulations/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=CongratulationResponseSchema)
    async def update_congratulation(
        self, data: Congratulation, **kwargs
    ) -> (int, CongratulationResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{data.occasion_id}/congratulations/{data.id}"),
            json=data.as_dict(),
            **kwargs,
        )
