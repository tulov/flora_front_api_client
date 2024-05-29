from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, DataRequest
from ..presentations.error import ErrorResponse
from ..presentations.todo import TodosResponse
from ..schemas.todos import TodosResponseSchema
from ..schemas import SuccessResponseSchema


class TodoNamespace(Namespace):
    URL = "/todos/"

    @expectations(schema=TodosResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, TodosResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def update(
        self, id_: int, data: DataRequest, **kwargs
    ) -> (int, TodosResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}"), json=data.as_dict(), **kwargs
        )
