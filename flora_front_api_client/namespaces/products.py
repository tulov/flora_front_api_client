from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.categories import FilterCounterRequest, FilterCounterResponse
from ..presentations.error import ErrorResponse
from ..presentations.products import (
    ProductResponse,
    ProductRequest,
    ProductsResponse,
    FeaturedProductsResponse,
    FeaturedProductsQuerystring,
    PreferredExecutorResponse,
    PreferredExecutorQuerystring,
    IdsFeaturedProductsQuerystring,
    SuccessFeaturedProductsResponse,
    DeliveryTimePeriodResponse,
    DeliveryTimePeriodRequest,
)
from ..schemas import (
    ProductResponseSchema,
    ProductsResponseSchema,
    FeaturedProductsResponseSchema,
    PreferredExecutorResponseSchema,
    SuccessFeaturedProductsResponseSchema,
    FilterCounterResponseSchema,
)
from ..schemas.products import DeliveryTimePeriodResponseSchema


class ProductsNamespace(Namespace):
    URL = "/products/"

    @expectations(schema=ProductResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: ProductRequest, **kwargs
    ) -> (int, ProductResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=ProductsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, ProductsResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=ProductResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, ProductResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=ProductResponseSchema)
    async def update(
        self, id_: int, data: ProductRequest, **kwargs
    ) -> (int, ProductResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=id_), json=data.as_dict(), **kwargs
        )

    @expectations(schema=FeaturedProductsResponseSchema)
    async def featured(
        self,
        city_id: int,
        # category: int | str,
        query_params: FeaturedProductsQuerystring = None,
        **kwargs,
    ) -> (int, FeaturedProductsResponse | ErrorResponse, RenewTokenResponse):
        postfix_url = f"featured/{city_id}"
        return await self._get(
            self.build_url(query_params, postfix_url=postfix_url), **kwargs
        )

    @expectations(schema=PreferredExecutorResponseSchema)
    async def preferred_executor(
        self,
        id_: int,
        city_id: int,
        query_params: PreferredExecutorQuerystring = None,
        **kwargs,
    ) -> (int, PreferredExecutorResponse | ErrorResponse, RenewTokenResponse):
        postfix_url = f"{id_}/preferred-executor/{city_id}"
        return await self._get(
            self.build_url(query_params, postfix_url=postfix_url), **kwargs
        )

    @expectations(schema=FeaturedProductsResponseSchema)
    async def simular(
        self,
        id_: int,
        city_id: int,
        query_params: PreferredExecutorQuerystring = None,
        **kwargs,
    ) -> (int, FeaturedProductsResponse | ErrorResponse, RenewTokenResponse):
        postfix_url = f"{id_}/simular/{city_id}"
        return await self._get(
            self.build_url(query_params, postfix_url=postfix_url), **kwargs
        )

    @expectations(schema=FeaturedProductsResponseSchema)
    async def concomitant_presents(
        self, city_id: int, query_params: FeaturedProductsQuerystring = None, **kwargs
    ) -> (int, FeaturedProductsResponse | ErrorResponse, RenewTokenResponse):
        postfix_url = f"concomitant-presents/{city_id}"
        return await self._get(
            self.build_url(query_params, postfix_url=postfix_url), **kwargs
        )

    @expectations(schema=SuccessFeaturedProductsResponseSchema)
    async def ids_featured(
        self,
        city_id: int,
        query_params: IdsFeaturedProductsQuerystring = None,
        **kwargs,
    ) -> (int, SuccessFeaturedProductsResponse | ErrorResponse, RenewTokenResponse):
        postfix_url = f"featured/{city_id}"
        return await self._get(
            self.build_url(query_params, postfix_url=postfix_url), **kwargs
        )

    @expectations(schema=DeliveryTimePeriodResponseSchema)
    async def delivery_time_period(
        self, data: DeliveryTimePeriodRequest, **kwargs
    ) -> (int, DeliveryTimePeriodResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url="delivery-time-period"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=FilterCounterResponseSchema)
    async def filter_counters(
        self, data: FilterCounterRequest, **kwargs
    ) -> (int, FilterCounterResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url="featured/filter-counter/"),
            json=data.as_dict(),
            **kwargs,
        )

