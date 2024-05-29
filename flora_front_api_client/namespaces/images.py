from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.images import ImageResponse, ImageUploadRequest
from ..schemas import ImageResponseSchema


class ImagesNamespace(Namespace):
    URL = "/images/"

    @expectations(schema=ImageResponseSchema, expected_code=HTTPStatus.CREATED)
    async def upload(
        self, data: ImageUploadRequest, **kwargs
    ) -> (int, ImageResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=ImageResponseSchema)
    async def get(
        self, id_: int, **kwargs
    ) -> (int, ImageResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(postfix_url=id_), **kwargs)
