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
)
from ..presentations.bills import (
    BillsResponse,
    BillResponse,
    BillPayRequest,
    BillPDFResponse,
)
from ..presentations.error import ErrorResponse
from ..schemas import (
    BillsResponseSchema,
    BillResponseSchema,
    ResultResponseSchema,
    SuccessResponseSchema,
    BillPDFResponseSchema,
)


class BillsNamespace(Namespace):
    URL = "/bills/"

    @expectations(schema=BillResponseSchema)
    async def get(
        self, guid: str, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, BillResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params, postfix_url=guid), **kwargs)

    @expectations(schema=BillsResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, BillsResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=ResultResponseSchema)
    async def pay(
        self, guid: str, pay_service: str, data: BillPayRequest, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{guid}/pay/{pay_service}"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema)
    async def get_pay(
        self, guid: str, pay_service: str, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f"{guid}/pay/{pay_service}"),
            **kwargs,
        )


    @expectations(schema=ResultResponseSchema)
    async def russian_federation(
        self, guid: str, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f"{guid}/RF"),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema)
    async def after3d(
        self, guid: str, pay_service: str, data: BillPayRequest, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{guid}/after3d/{pay_service}"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=ResultResponseSchema)
    async def sign(
        self, guid: str, pay_service: str, **kwargs
    ) -> (int, ResultResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f"{guid}/sign/{pay_service}"), **kwargs
        )

    @expectations(schema=SuccessResponseSchema)
    async def post_pay(
        self, guid: str, pay_service: str, flag: str, data: Any = None, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        if data is None:
            data = {}
        return await self._post(
            self.build_url(postfix_url=f"{guid}/post/{pay_service}/{flag}"),
            json=data,
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def pdf_send_to_email(
        self, guid: str, pay_service: str, data: DataRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{guid}/pdf/{pay_service}/send-email"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=BillPDFResponseSchema)
    async def pdf(
        self, guid: str, pay_service: str, data: DataRequest, **kwargs
    ) -> (int, BillPDFResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{guid}/pdf/{pay_service}"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def send_link(
        self, guid: str, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{guid}/send-pay-link"), json={}, **kwargs
        )
