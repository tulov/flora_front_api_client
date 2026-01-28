from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.error import ErrorResponse
from ..presentations.inflects import InflectRequest, InflectResponse
from ..schemas.inflects import InflectResponseSchema


class InflectsNamespace(Namespace):
    URL = "/inflects/"

    @expectations(schema=InflectResponseSchema)
    async def get(
        self, query_params: InflectRequest, **kwargs
    ) -> (int, InflectResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)
