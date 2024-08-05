from http import HTTPStatus
from typing import Any

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import (
    WithFieldsQuerystring,
    Querystring,
    ResultResponse,
    SuccessResponse,
    DataRequest,
    RevisionRequest,
)
from ..presentations.error import ErrorResponse
from ..presentations.orders import (
    LastDeliveryOrdersResponse,
    OrderResponse,
    CreateOrderRequest,
    OrdersResponse,
    OrderCommentRequest,
    OrderCommentResponse,
    OrderBillResponse,
    OrderBillRequest,
    AfterRejectRequestBody,
    OrderAnswerResponse,
    CancelOrderCalculationResponse,
    CancelOrderCalculation,
)
from ..schemas import (
    OrderResponseSchema,
    OrdersResponseSchema,
    OrderCommentResponseSchema,
    OrderBillResponseSchema,
    ResultResponseSchema,
    SuccessResponseSchema,
)
from ..schemas.orders import (
    OrderAnswerResponseSchema,
    CancelOrderCalculationResponseSchema,
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
        return await self._get(self.build_url(postfix_url='last_delivery_orders'), **kwargs)

    @expectations(schema=OrdersResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, OrdersResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=OrderCommentResponseSchema, expected_code=HTTPStatus.CREATED)
    async def comment(
        self, order_id: int, data: OrderCommentRequest, **kwargs
    ) -> (int, OrderCommentResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{order_id}/comments/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=OrderBillResponseSchema, expected_code=HTTPStatus.CREATED)
    async def bill(
        self, order_id: int, data: OrderBillRequest, **kwargs
    ) -> (int, OrderBillResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{order_id}/bills/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema)
    async def accept(
        self, order_id: int, data: RevisionRequest, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/accept/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema)
    async def reject(
        self, order_id: int, data: RevisionRequest, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/reject/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema)
    async def delivered(
        self, order_id: int, data: RevisionRequest, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/delivered/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema)
    async def on_delivery(
        self, order_id: int, data: DataRequest, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/on-delivery/"),
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

    @expectations(schema=ResultResponseSchema)
    async def after_reject(
        self, order_id: int, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/after-reject/"), json={}, **kwargs
        )

    @expectations(schema=SuccessResponseSchema)
    async def accept_after_reject(
        self, order_id: int, data: AfterRejectRequestBody, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/accept-after-reject/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def reject_after_reject(
        self, order_id: int, data: AfterRejectRequestBody, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/reject-after-reject/"),
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

    @expectations(schema=SuccessResponseSchema)
    async def unbind_photo(
        self, order_id: int, photo_id: int, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/unbind-photo/{photo_id}"),
            json={},
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def send_photos_before_delivery(
        self, order_id: int, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{order_id}/send-photo-before-delivery/"),
            json={},
            **kwargs,
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

    @expectations(schema=CancelOrderCalculationResponseSchema)
    async def calculate_for_cancel(
        self, order_id: int, **kwargs
    ) -> (int, CancelOrderCalculationResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f"{order_id}/cancel-calculate/"),
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def cancel(
        self, data: CancelOrderCalculation, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{data.order_id}/cancel/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema, expected_code=HTTPStatus.CREATED)
    async def dispute(
        self, order_id: int, data: DataRequest, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{order_id}/dispute/"),
            json=data.as_dict(),
            **kwargs,
        )
