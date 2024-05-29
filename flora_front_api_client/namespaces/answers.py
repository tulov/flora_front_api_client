from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.error import ErrorResponse
from ..presentations.orders import AnswerResponse, AnswersResponse
from ..schemas.orders import AnswerResponseSchema, AnswersResponseSchema


class AnswersNamespace(Namespace):
    URL = "/answers/"

    @expectations(schema=AnswersResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, AnswersResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=AnswerResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, AnswerResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=AnswerResponseSchema)
    async def toggle(
        self, id_: int, **kwargs
    ) -> (int, AnswerResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}/toggle"), json={}, **kwargs
        )
