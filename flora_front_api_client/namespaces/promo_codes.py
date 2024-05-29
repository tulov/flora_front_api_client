from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.promo import (
    PromoCode, PromoCodesResponse, PromoCodeResponse
)
from ..presentations.error import ErrorResponse
from ..schemas.promo import (
    PromoCodeResponseSchema, PromoCodesResponseSchema
)
from ..namespaces.base import Namespace


class PromoCodesNamespace(Namespace):
    URL = '/promo-codes/'

    @expectations(schema=PromoCodeResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: PromoCode, **kwargs
    ) -> (int, Union[PromoCodeResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=PromoCodeResponseSchema)
    async def update(
        self, code: str, data: PromoCode, **kwargs
    ) -> (int, Union[PromoCodeResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=code),
                               json=data.as_dict(), **kwargs)

    @expectations(schema=PromoCodesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[PromoCodesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=PromoCodeResponseSchema)
    async def get(
        self, code: str, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[PromoCodeResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=code), **kwargs)
