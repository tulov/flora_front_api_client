from http import HTTPStatus
from typing import Any

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import (
    WithFieldsQuerystring,
    Querystring,
    SuccessResponse,
    DataRequest,
)
from ..presentations.error import ErrorResponse
from ..presentations.orders import (
    LastDeliveryOrdersResponse,
    OrderResponse,
    CreateOrderRequest,
    OrdersResponse,
    OrderBillResponse,
    OrderBillRequest,
    OrderAnswerResponse,
)
from ..schemas import (
    OrderResponseSchema,
    OrdersResponseSchema,
    OrderBillResponseSchema,
    SuccessResponseSchema,
)
from ..schemas.orders import (
    OrderAnswerResponseSchema,
    LastDeliveryOrdersResponseSchema,
)


class OrdersNamespace(Namespace):
    URL = "/orders/"

    @expectations(schema=OrderResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CreateOrderRequest, **kwargs
    ) -> (int, OrderResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=OrderResponseSchema)
    async def get(
        self,
        id_: int,
        query_params: WithFieldsQuerystring | dict[str, Any] = None,
        **kwargs,
    ) -> (int, OrderResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=LastDeliveryOrdersResponseSchema)
    async def last_delivery_orders(
        self,
        **kwargs,
    ) -> (int, LastDeliveryOrdersResponse | ErrorResponse):
        return await self._get(
            self.build_url(postfix_url="last_delivery_orders"), **kwargs
        )

    @expectations(schema=OrdersResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, OrdersResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=OrderBillResponseSchema, expected_code=HTTPStatus.CREATED)
    async def bill(
        self, order_id: int, data: OrderBillRequest, **kwargs
    ) -> (int, OrderBillResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{order_id}/bills/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def exact_delivery_time(
        self, order_id: int, data: DataRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/exact-delivery-time/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def update(
        self, order_id: int, data: DataRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}"), json=data.as_dict(), **kwargs
        )

    @expectations(schema=SuccessResponseSchema, expected_code=HTTPStatus.CREATED)
    async def create_answer(
        self, order_id: int, data: DataRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{order_id}/answers/"),
            json=data.data,
            **kwargs,
        )

    @expectations(schema=OrderAnswerResponseSchema)
    async def answers(
        self, order_id: int, **kwargs
    ) -> (int, OrderAnswerResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f"{order_id}/answers/"),
            **kwargs,
        )
