from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import (
    AuthResponse, AuthRequest, RenewTokenRequest, RenewTokenResponse,
    SendRestoreAccessLinkRequest, RestoreAccessRequest, EnterCodeRequest,
    AuthCodeRequest
)
from ..presentations.error import ErrorResponse
from ..presentations.base import SuccessResponse
from ..schemas import (
    AuthResponseSchema, RenewTokenResponseSchema, SuccessResponseSchema,
)
from ..namespaces.base import Namespace


class AuthNamespace(Namespace):
    URL = '/auth/'

    @expectations(schema=AuthResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def authenticate(
        self, data: AuthRequest, **kwargs
    ) -> (int, Union[AuthResponse, ErrorResponse], RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=RenewTokenResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def renew(
        self, data: RenewTokenRequest, **kwargs
    ) -> (int, Union[RenewTokenResponse, ErrorResponse], RenewTokenResponse):
        return await self._post(f'{self.URL}renew/',
                                json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def send_restore_access_link(
        self, data: SendRestoreAccessLinkRequest, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse], RenewTokenResponse):
        return await self._post(f'{self.URL}send-restore-access-link/',
                                json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema,
                  expected_code=HTTPStatus.OK)
    async def restore_access(
        self, data: RestoreAccessRequest, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse], RenewTokenResponse):
        return await self._put(f'{self.URL}restore-access/',
                               json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def code(
        self, data: EnterCodeRequest, **kwargs
    ) -> (int, Union[SuccessResponse, ErrorResponse], RenewTokenResponse):
        return await self._post(f'{self.URL}code/',
                                json=data.as_dict(), **kwargs)

    @expectations(schema=AuthResponseSchema)
    async def auth_with_code(
        self, data: AuthCodeRequest, **kwargs
    ) -> (int, Union[AuthResponse, ErrorResponse], RenewTokenResponse):
        return await self._post(f'{self.URL}with-code/',
                                json=data.as_dict(), **kwargs)

