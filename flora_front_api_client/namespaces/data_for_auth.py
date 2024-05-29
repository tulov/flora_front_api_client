from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.users import (
    ConfirmDataForAuthRequest
)
from ..presentations.base import SuccessResponse
from ..schemas import SuccessResponseSchema
from ..namespaces.base import Namespace


class DataForAuthNamespace(Namespace):
    URL = '/data_for_auth/'

    @expectations(schema=SuccessResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def confirm(
        self, data_id: int, data: ConfirmDataForAuthRequest, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(f'{self.URL}{data_id}/confirm/',
                               json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def resend(self, data_id: int, **kwargs
                     ) -> (int, Union[SuccessResponse, ErrorResponse],
                           RenewTokenResponse):
        return await self._put(f'{self.URL}{data_id}/send/', **kwargs)
